# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3292
- Title: REPORT Act
- Congress: 119
- Bill type: HR
- Bill number: 3292
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-04-16T14:44:09Z
- Update date including text: 2026-04-16T14:44:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3292",
    "number": "3292",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "REPORT Act",
    "type": "HR",
    "updateDate": "2026-04-16T14:44:09Z",
    "updateDateIncludingText": "2026-04-16T14:44:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3292ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3292\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mrs. Kim (for herself and Mr. Hurd of Colorado ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the publication of a detailed justification with respect to certain tariff modifications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reviewing Economic and Protection Objectives for Reciprocal Tariffs Act or the REPORT Act .\n#### 2. Report required\n##### (a) Public notice\nNot later than 48 hours before the entry into effect of any increase or decrease in a duty pursuant to a provision of law or regulation authorizing modifications on an emergency or discretionary basis to duties imposed on articles imported into the United States, the President shall publish in the Federal Register\u2014\n**(1)**\nnotice of such determination; and\n**(2)**\na detailed justification for such increase or decrease.\n##### (b) Briefing\nNot later than 7 days after the date on which the President makes a determination to modify a duty pursuant to an authority described in subsection (a), the United States Trade Representative shall brief the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate on such determination, including the justification for such determination.",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in House"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-06-05T15:01:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119hr3292",
          "measure-number": "3292",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-08",
          "originChamber": "HOUSE",
          "update-date": "2026-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3292v00",
            "update-date": "2026-04-16"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reviewing Economic and Protection Objectives for Reciprocal Tariffs Act or the REPORT Act</strong></p><p>This bill requires public and congressional\u00a0notification of certain increases or decreases in a duty\u00a0(i.e., tariff) imposed by the President on articles imported into the United States.\u00a0</p><p>Specifically, the President must publish information in the Federal Register within 48 hours of increasing or decreasing a duty on articles imported into the United States\u00a0pursuant to a law or regulation authorizing modifications to duties on an emergency or discretionary basis. This publication must include (1) notice of such determination, and (2) a detailed justification for such increase or decrease.</p><p>Additionally, the Office of the U.S. Trade Representative must brief specified congressional committees within seven days of the President making a determination to modify a duty. The briefing must include the justification for the President's determination.</p>"
        },
        "title": "REPORT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3292.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reviewing Economic and Protection Objectives for Reciprocal Tariffs Act or the REPORT Act</strong></p><p>This bill requires public and congressional\u00a0notification of certain increases or decreases in a duty\u00a0(i.e., tariff) imposed by the President on articles imported into the United States.\u00a0</p><p>Specifically, the President must publish information in the Federal Register within 48 hours of increasing or decreasing a duty on articles imported into the United States\u00a0pursuant to a law or regulation authorizing modifications to duties on an emergency or discretionary basis. This publication must include (1) notice of such determination, and (2) a detailed justification for such increase or decrease.</p><p>Additionally, the Office of the U.S. Trade Representative must brief specified congressional committees within seven days of the President making a determination to modify a duty. The briefing must include the justification for the President's determination.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119hr3292"
    },
    "title": "REPORT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reviewing Economic and Protection Objectives for Reciprocal Tariffs Act or the REPORT Act</strong></p><p>This bill requires public and congressional\u00a0notification of certain increases or decreases in a duty\u00a0(i.e., tariff) imposed by the President on articles imported into the United States.\u00a0</p><p>Specifically, the President must publish information in the Federal Register within 48 hours of increasing or decreasing a duty on articles imported into the United States\u00a0pursuant to a law or regulation authorizing modifications to duties on an emergency or discretionary basis. This publication must include (1) notice of such determination, and (2) a detailed justification for such increase or decrease.</p><p>Additionally, the Office of the U.S. Trade Representative must brief specified congressional committees within seven days of the President making a determination to modify a duty. The briefing must include the justification for the President's determination.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119hr3292"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3292ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "REPORT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPORT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reviewing Economic and Protection Objectives for Reciprocal Tariffs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the publication of a detailed justification with respect to certain tariff modifications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:31Z"
    }
  ]
}
```
