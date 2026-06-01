# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/10?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/10
- Title: HEALTH Act
- Congress: 119
- Bill type: HRES
- Bill number: 10
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-30T13:09:54Z
- Update date including text: 2025-01-30T13:09:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/10",
    "number": "10",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "HEALTH Act",
    "type": "HRES",
    "updateDate": "2025-01-30T13:09:54Z",
    "updateDateIncludingText": "2025-01-30T13:09:54Z"
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
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-03T16:15:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres10ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 10\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Davidson submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to establish a Committee on Health as a standing committee of the House.\n#### 1. Short title\nThis resolution may be cited as the House Endeavor to Accelerate a Legislative Transformation of Healthcare Act or the HEALTH Act .\n#### 2. Establishment of Committee on Health\n##### (a) In general\nClause 1 of rule X of the Rules of the House of Representatives is amended\u2014\n**(1)**\nby redesignating paragraphs (j) through (t) as paragraphs (k) through (u); and\n**(2)**\nby inserting after paragraph (i) the following new paragraph:\n(j) Committee on Health (A) Biomedical research and development, including the Food and Drug Administration. (B) Health, health facilities, and health care supported by general revenues (except veterans\u2019 hospitals, medical care, and treatment of veterans). (C) Public health and quarantine, including the Centers for Disease Control and Prevention. .\n##### (b) Conforming amendments to existing jurisdiction of standing committees\n**(1) Committee on Education and the Workforce**\nClause 1(e)(6) of such rule is amended by striking generally and inserting generally (except health insurance programs) .\n**(2) Committee on Energy and Commerce**\nClause 1(f) of such rule is amended\u2014\n**(A)**\nby striking subparagraphs (1), (3), and (12); and\n**(B)**\nby redesignating the remaining subparagraphs accordingly.",
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
            "name": "Centers for Disease Control and Prevention (CDC)",
            "updateDate": "2025-01-15T18:59:14Z"
          },
          {
            "name": "Congressional committees",
            "updateDate": "2025-01-15T18:58:34Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-01-15T18:58:46Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-01-15T18:59:19Z"
          },
          {
            "name": "Food and Drug Administration (FDA)",
            "updateDate": "2025-01-15T18:59:10Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-01-15T18:59:06Z"
          },
          {
            "name": "House Committee on Education and Workforce",
            "updateDate": "2025-01-30T13:09:54Z"
          },
          {
            "name": "House Committee on Energy and Commerce",
            "updateDate": "2025-01-15T18:59:00Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:58:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-08T18:48:45Z"
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
          "measure-id": "id119hres10",
          "measure-number": "10",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres10v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>House Endeavor to Accelerate a Legislative Transformation of Healthcare Act or the HEALTH Act</strong></p><p>This resolution establishes the Committee on Health, a standing committee of the House of Representatives, and specifies the subjects within its jurisdiction.\u00a0</p><p>The Committee on Health is responsible for all legislation and other matters relating to biomedical research and development (including the Food and Drug Administration); health, health facilities, and health care supported by general revenues (except veterans\u2019 hospitals, medical care, and treatment); and public health and quarantine (including the Centers for Disease Control and Prevention). The resolution also removes these topics from the jurisdiction of the Committee on Education and the Workforce and the Committee on Energy and Commerce.</p>"
        },
        "title": "HEALTH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres10.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>House Endeavor to Accelerate a Legislative Transformation of Healthcare Act or the HEALTH Act</strong></p><p>This resolution establishes the Committee on Health, a standing committee of the House of Representatives, and specifies the subjects within its jurisdiction.\u00a0</p><p>The Committee on Health is responsible for all legislation and other matters relating to biomedical research and development (including the Food and Drug Administration); health, health facilities, and health care supported by general revenues (except veterans\u2019 hospitals, medical care, and treatment); and public health and quarantine (including the Centers for Disease Control and Prevention). The resolution also removes these topics from the jurisdiction of the Committee on Education and the Workforce and the Committee on Energy and Commerce.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hres10"
    },
    "title": "HEALTH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>House Endeavor to Accelerate a Legislative Transformation of Healthcare Act or the HEALTH Act</strong></p><p>This resolution establishes the Committee on Health, a standing committee of the House of Representatives, and specifies the subjects within its jurisdiction.\u00a0</p><p>The Committee on Health is responsible for all legislation and other matters relating to biomedical research and development (including the Food and Drug Administration); health, health facilities, and health care supported by general revenues (except veterans\u2019 hospitals, medical care, and treatment); and public health and quarantine (including the Centers for Disease Control and Prevention). The resolution also removes these topics from the jurisdiction of the Committee on Education and the Workforce and the Committee on Energy and Commerce.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hres10"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres10ih.xml"
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
      "title": "HEALTH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:57Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amending the Rules of the House of Representatives to establish a Committee on Health as a standing committee of the House.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:57Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEALTH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-06T13:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "House Endeavor to Accelerate a Legislative Transformation of Healthcare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-06T13:23:14Z"
    }
  ]
}
```
