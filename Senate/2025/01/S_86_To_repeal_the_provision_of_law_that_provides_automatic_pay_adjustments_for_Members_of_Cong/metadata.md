# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/86?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/86
- Title: A bill to repeal the provision of law that provides automatic pay adjustments for Members of Congress.
- Congress: 119
- Bill type: S
- Bill number: 86
- Origin chamber: Senate
- Introduced date: 2025-01-14
- Update date: 2026-03-11T14:52:21Z
- Update date including text: 2026-03-11T14:52:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in Senate
- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-14: Introduced in Senate

## Actions

- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/86",
    "number": "86",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A bill to repeal the provision of law that provides automatic pay adjustments for Members of Congress.",
    "type": "S",
    "updateDate": "2026-03-11T14:52:21Z",
    "updateDateIncludingText": "2026-03-11T14:52:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T19:50:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s86is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 86\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo repeal the provision of law that provides automatic pay adjustments for Members of Congress.\n#### 1. Elimination of automatic pay adjustments for Members of Congress\n##### (a) In general\nParagraph (2) of section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ) is repealed.\n##### (b) Technical and conforming amendments\nSection 601(a) of such Act ( 2 U.S.C. 4501 ) is amended\u2014\n**(1)**\nby striking (a)(1) and inserting (a) ;\n**(2)**\nby redesignating subparagraphs (A), (B), and (C) as paragraphs (1), (2), and (3), respectively; and\n**(3)**\nby striking as adjusted by paragraph (2) of this subsection and inserting adjusted as provided by law .\n##### (c) Effective date\nThis section and the amendments made by this section shall take effect on the date on which the 120th Congress convenes.",
      "versionDate": "2025-01-14",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-20",
        "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7628",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To repeal the provision of law that provides automatic pay adjustments for Members of Congress.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-13",
        "text": "Referred to the Committee on House Administration, and in addition to the Committees on Ways and Means, the Judiciary, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "358",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Corruption in Government Act",
      "type": "HR"
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
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-03T18:52:37Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-03-03T18:52:37Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-03T18:52:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-11T17:13:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119s86",
          "measure-number": "86",
          "measure-type": "s",
          "orig-publish-date": "2025-01-14",
          "originChamber": "SENATE",
          "update-date": "2025-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s86v00",
            "update-date": "2025-04-21"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill eliminates automatic increases to pay\u00a0for Members of Congress, beginning with the 120th Congress. </p><p>Current law automatically increases Member\u00a0pay according to a formula. The annual increase is (1) based on the percentage change in private sector wages as measured by the Employment Cost Index (ECI); and (2) capped at the percentage increase to General Schedule (GS) employees' base pay.\u00a0The annual adjustment automatically goes into effect unless Congress modifies the increase in legislation.</p>"
        },
        "title": "A bill to repeal the provision of law that provides automatic pay adjustments for Members of Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s86.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill eliminates automatic increases to pay\u00a0for Members of Congress, beginning with the 120th Congress. </p><p>Current law automatically increases Member\u00a0pay according to a formula. The annual increase is (1) based on the percentage change in private sector wages as measured by the Employment Cost Index (ECI); and (2) capped at the percentage increase to General Schedule (GS) employees' base pay.\u00a0The annual adjustment automatically goes into effect unless Congress modifies the increase in legislation.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119s86"
    },
    "title": "A bill to repeal the provision of law that provides automatic pay adjustments for Members of Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill eliminates automatic increases to pay\u00a0for Members of Congress, beginning with the 120th Congress. </p><p>Current law automatically increases Member\u00a0pay according to a formula. The annual increase is (1) based on the percentage change in private sector wages as measured by the Employment Cost Index (ECI); and (2) capped at the percentage increase to General Schedule (GS) employees' base pay.\u00a0The annual adjustment automatically goes into effect unless Congress modifies the increase in legislation.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119s86"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s86is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the provision of law that provides automatic pay adjustments for Members of Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:31Z"
    },
    {
      "title": "A bill to repeal the provision of law that provides automatic pay adjustments for Members of Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-15T11:56:20Z"
    }
  ]
}
```
