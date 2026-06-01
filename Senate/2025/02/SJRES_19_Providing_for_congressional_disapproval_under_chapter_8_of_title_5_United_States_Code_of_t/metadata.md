# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/19?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/19
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)".
- Congress: 119
- Bill type: SJRES
- Bill number: 19
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-03-17T18:44:44Z
- Update date including text: 2025-03-17T18:44:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/19",
    "number": "19",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\".",
    "type": "SJRES",
    "updateDate": "2025-03-17T18:44:44Z",
    "updateDateIncludingText": "2025-03-17T18:44:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T16:29:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres19is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 19\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Kennedy introduced the following joint resolution; which was read twice and referred to the Committee on Environment and Public Works\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA) .\nThat Congress disapproves the rule submitted by the Environmental Protection Agency relating to Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA) (89 Fed. Reg. 102568 (December 17, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-13",
      "versionType": "IS"
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "34",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\".",
      "type": "HJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "27",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\".",
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
        "name": "Environmental Protection",
        "updateDate": "2025-02-18T13:42:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119sjres19",
          "measure-number": "19",
          "measure-type": "sjres",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres19v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the Environmental Protection Agency rule titled <em>Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)</em> (89 Fed. Reg. 102568) and published on December 17, 2024. Among other elements, the rule prohibits the manufacturing, import, processing, and distribution in commerce of trichloroethylene (TCE) for all uses (including consumer uses), and prohibits the industrial and commercial use of TCE.</p>"
        },
        "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres19.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency rule titled <em>Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)</em> (89 Fed. Reg. 102568) and published on December 17, 2024. Among other elements, the rule prohibits the manufacturing, import, processing, and distribution in commerce of trichloroethylene (TCE) for all uses (including consumer uses), and prohibits the industrial and commercial use of TCE.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119sjres19"
    },
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency rule titled <em>Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)</em> (89 Fed. Reg. 102568) and published on December 17, 2024. Among other elements, the rule prohibits the manufacturing, import, processing, and distribution in commerce of trichloroethylene (TCE) for all uses (including consumer uses), and prohibits the industrial and commercial use of TCE.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119sjres19"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres19is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-15T05:18:32Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Trichloroethylene (TCE); Regulation Under the Toxic Substances Control Act (TSCA)\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:56:25Z"
    }
  ]
}
```
