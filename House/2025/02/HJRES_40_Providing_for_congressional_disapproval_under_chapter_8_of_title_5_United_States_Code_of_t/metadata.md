# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/40?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/40
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to "Cybersecurity Maturity Model Certification (CMMC) Program".
- Congress: 119
- Bill type: HJRES
- Bill number: 40
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-06-13T18:51:07Z
- Update date including text: 2025-06-13T18:51:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/40",
    "number": "40",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001116",
        "district": "9",
        "firstName": "Andrew",
        "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
        "lastName": "Clyde",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to \"Cybersecurity Maturity Model Certification (CMMC) Program\".",
    "type": "HJRES",
    "updateDate": "2025-06-13T18:51:07Z",
    "updateDateIncludingText": "2025-06-13T18:51:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres40ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 40\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Clyde submitted the following joint resolution; which was referred to the Committee on Armed Services\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to Cybersecurity Maturity Model Certification (CMMC) Program .\nThat Congress disapproves the rule submitted by the Department of Defense relating to Cybersecurity Maturity Model Certification (CMMC) Program (89 Fed. Reg. 83092 (October 15, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-12",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-13T18:50:30Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-06-13T18:50:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:50:36Z"
          },
          {
            "name": "Department of Defense",
            "updateDate": "2025-06-13T18:50:44Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-06-13T18:51:07Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-06-13T18:51:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T18:26:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hjres40",
          "measure-number": "40",
          "measure-type": "hjres",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres40v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the Department of Defense (DOD) rule titled <em>Cybersecurity Maturity Model Certification (CMMC) Program</em> (89 Fed. Reg. 83092) and published on October 15, 2024. Among other elements, the rule establishes the\u00a0Cybersecurity Maturity Model Certification Program. The program institutes\u00a0policies regarding the protection of Federal Contract Information (FCI) and Controlled Unclassified Information (CUI) that is processed, stored, or transmitted on defense contractor and subcontractor information systems during defense contract performance. The rule also identifies entities to which the rule applies and describes DOD implementation of the program.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to \"Cybersecurity Maturity Model Certification (CMMC) Program\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres40.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Department of Defense (DOD) rule titled <em>Cybersecurity Maturity Model Certification (CMMC) Program</em> (89 Fed. Reg. 83092) and published on October 15, 2024. Among other elements, the rule establishes the\u00a0Cybersecurity Maturity Model Certification Program. The program institutes\u00a0policies regarding the protection of Federal Contract Information (FCI) and Controlled Unclassified Information (CUI) that is processed, stored, or transmitted on defense contractor and subcontractor information systems during defense contract performance. The rule also identifies entities to which the rule applies and describes DOD implementation of the program.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hjres40"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to \"Cybersecurity Maturity Model Certification (CMMC) Program\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Department of Defense (DOD) rule titled <em>Cybersecurity Maturity Model Certification (CMMC) Program</em> (89 Fed. Reg. 83092) and published on October 15, 2024. Among other elements, the rule establishes the\u00a0Cybersecurity Maturity Model Certification Program. The program institutes\u00a0policies regarding the protection of Federal Contract Information (FCI) and Controlled Unclassified Information (CUI) that is processed, stored, or transmitted on defense contractor and subcontractor information systems during defense contract performance. The rule also identifies entities to which the rule applies and describes DOD implementation of the program.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hjres40"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres40ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to \"Cybersecurity Maturity Model Certification (CMMC) Program\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:32Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Defense relating to \"Cybersecurity Maturity Model Certification (CMMC) Program\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:06:47Z"
    }
  ]
}
```
