# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/172
- Title: Defund Heroin Injection Centers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 172
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-14T16:37:19Z
- Update date including text: 2026-01-14T16:37:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/172",
    "number": "172",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Defund Heroin Injection Centers Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T16:37:19Z",
    "updateDateIncludingText": "2026-01-14T16:37:19Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
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
          "date": "2025-01-03T16:26:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr172ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 172\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit Federal funds for any State, local, Tribal, or private entity that operates or controls an injection center in violation of section 416 of the Controlled Substances Act ( 21 U.S.C. 856 ; commonly referred to as the Crack House Statute ).\n#### 1. Short title\nThis Act may be cited as the Defund Heroin Injection Centers Act of 2025 .\n#### 2. No Federal funds for entities operating unlawful injection centers\nNo Federal funds may be made available to any State, local, Tribal, or private entity that operates or controls an injection center in violation of section 416 of the Controlled Substances Act ( 21 U.S.C. 856 ; commonly referred to as the Crack House Statute ).",
      "versionDate": "2025-01-03",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-14T16:37:19Z"
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
          "measure-id": "id119hr172",
          "measure-number": "172",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr172v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Defund Heroin Injection Centers Act of 2025</strong></p><p>This bill prohibits federal funds from being made available to a state, local, tribal, or private entity that operates or controls an injection center (i.e., a medically supervised injection site) in violation of the federal statute commonly known as the Crack House Statute. The statute generally prohibits making facilities available for the purpose of unlawfully using a controlled substance. </p>"
        },
        "title": "Defund Heroin Injection Centers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr172.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defund Heroin Injection Centers Act of 2025</strong></p><p>This bill prohibits federal funds from being made available to a state, local, tribal, or private entity that operates or controls an injection center (i.e., a medically supervised injection site) in violation of the federal statute commonly known as the Crack House Statute. The statute generally prohibits making facilities available for the purpose of unlawfully using a controlled substance. </p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr172"
    },
    "title": "Defund Heroin Injection Centers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defund Heroin Injection Centers Act of 2025</strong></p><p>This bill prohibits federal funds from being made available to a state, local, tribal, or private entity that operates or controls an injection center (i.e., a medically supervised injection site) in violation of the federal statute commonly known as the Crack House Statute. The statute generally prohibits making facilities available for the purpose of unlawfully using a controlled substance. </p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr172"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr172ih.xml"
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
      "title": "Defund Heroin Injection Centers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defund Heroin Injection Centers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funds for any State, local, Tribal, or private entity that operates or controls an injection center in violation of section 416 of the Controlled Substances Act (21 U.S.C. 856; commonly referred to as the \"Crack House Statute\").",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:25Z"
    }
  ]
}
```
