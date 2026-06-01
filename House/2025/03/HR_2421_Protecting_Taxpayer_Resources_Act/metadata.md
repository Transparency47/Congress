# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2421?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2421
- Title: Protecting Taxpayer Resources Act
- Congress: 119
- Bill type: HR
- Bill number: 2421
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-04-09T14:10:50Z
- Update date including text: 2026-04-09T14:10:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2421",
    "number": "2421",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000617",
        "district": "1",
        "firstName": "Suzan",
        "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
        "lastName": "DelBene",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Protecting Taxpayer Resources Act",
    "type": "HR",
    "updateDate": "2026-04-09T14:10:50Z",
    "updateDateIncludingText": "2026-04-09T14:10:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:10Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2421ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2421\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. DelBene (for herself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require a certain determination by the Treasury Inspector General for Tax Administration regarding the imposition on personnel of the Internal Revenue Service a function of the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Taxpayer Resources Act .\n#### 2. Determination regarding the imposition of certain homeland security functions on personnel of the Internal Revenue Service\n##### (a) In general\nNotwithstanding any other provision of law, a function of the Department of Homeland Security may not be imposed on personnel of the Internal Revenue Service unless the Treasury Inspector General for Tax Administration makes a determination regarding the following:\n**(1)**\nThat such personnel have been trained to administer such function.\n**(2)**\nThat imposing such function on such personnel would not impede the administration of the Service, including relating to the following:\n**(A)**\nProviding quality service to taxpayers (as such term is defined in section 7701 of the Internal Revenue Code of 1986) by helping taxpayers understand and meet tax responsibilities.\n**(B)**\nEnforcing applicable law with integrity and fairness to all taxpayers.\n##### (b) Federal Register\nA determination under subsection (a) shall be effective upon publication in the Federal Register, and the Treasury Inspector General for Tax Administration may terminate such determination in the same manner.\n##### (c) Conforming amendment\nSection 428(b) of the Homeland Security Act of 2002 ( 6 U.S.C. 236(b) ) is amended, in the matter preceding paragraph (1), by inserting the Protecting Taxpayer Resources Act or after in .",
      "versionDate": "2025-03-27",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T15:11:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2421",
          "measure-number": "2421",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2421v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Taxpayer Resources Act</strong></p><p>This bill provides that Department of Homeland Security functions (e.g., immigration enforcement) may not be assigned to Internal Revenue Service\u00a0(IRS) personnel (e.g., IRS criminal investigators) unless the Treasury Inspector General for Tax Administration determines (1) such IRS personnel are trained to administer such functions, and (2) the imposition of such functions on IRS personnel will not impede the IRS from enforcing federal tax law and\u00a0providing quality services to taxpayers.\u00a0\u00a0</p>"
        },
        "title": "Protecting Taxpayer Resources Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2421.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Taxpayer Resources Act</strong></p><p>This bill provides that Department of Homeland Security functions (e.g., immigration enforcement) may not be assigned to Internal Revenue Service\u00a0(IRS) personnel (e.g., IRS criminal investigators) unless the Treasury Inspector General for Tax Administration determines (1) such IRS personnel are trained to administer such functions, and (2) the imposition of such functions on IRS personnel will not impede the IRS from enforcing federal tax law and\u00a0providing quality services to taxpayers.\u00a0\u00a0</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr2421"
    },
    "title": "Protecting Taxpayer Resources Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Taxpayer Resources Act</strong></p><p>This bill provides that Department of Homeland Security functions (e.g., immigration enforcement) may not be assigned to Internal Revenue Service\u00a0(IRS) personnel (e.g., IRS criminal investigators) unless the Treasury Inspector General for Tax Administration determines (1) such IRS personnel are trained to administer such functions, and (2) the imposition of such functions on IRS personnel will not impede the IRS from enforcing federal tax law and\u00a0providing quality services to taxpayers.\u00a0\u00a0</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr2421"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2421ih.xml"
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
      "title": "Protecting Taxpayer Resources Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Taxpayer Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a certain determination by the Treasury Inspector General for Tax Administration regarding the imposition on personnel of the Internal Revenue Service a function of the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:27Z"
    }
  ]
}
```
