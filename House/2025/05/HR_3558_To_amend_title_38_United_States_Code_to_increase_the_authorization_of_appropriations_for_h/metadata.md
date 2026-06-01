# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3558
- Title: Veteran Jobs Training Act
- Congress: 119
- Bill type: HR
- Bill number: 3558
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-12-12T09:08:03Z
- Update date including text: 2025-12-12T09:08:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3558",
    "number": "3558",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Veteran Jobs Training Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:08:03Z",
    "updateDateIncludingText": "2025-12-12T09:08:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:43:52Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3558ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3558\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Neguse introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to increase the authorization of appropriations for homeless veterans reintegration programs.\n#### 1. Short Title\nThis Act may be cited as the Veteran Jobs Training Act .\n#### 2. Increase of authorization of appropriations for homeless veterans reintegration programs\nSection 2021(i)(1) of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (G), by striking fiscal year 2024 and each fiscal year thereafter and inserting each of fiscal years 2024 and 2025 ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(H) $75,000,000 for fiscal year 2024 and each fiscal year thereafter. .",
      "versionDate": "2025-05-21",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-05T18:37:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119hr3558",
          "measure-number": "3558",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3558v00",
            "update-date": "2025-08-14"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veteran Jobs Training Act</strong></p><p>This bill increases by $15 million funding for homeless veterans reintegration programs for FY2024 and each fiscal year thereafter. Such programs, administered by the Department of Labor, provide job training, counseling, and job placement services for certain veterans, including veterans who are homeless or transitioning from being incarcerated.</p>"
        },
        "title": "Veteran Jobs Training Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3558.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran Jobs Training Act</strong></p><p>This bill increases by $15 million funding for homeless veterans reintegration programs for FY2024 and each fiscal year thereafter. Such programs, administered by the Department of Labor, provide job training, counseling, and job placement services for certain veterans, including veterans who are homeless or transitioning from being incarcerated.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr3558"
    },
    "title": "Veteran Jobs Training Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran Jobs Training Act</strong></p><p>This bill increases by $15 million funding for homeless veterans reintegration programs for FY2024 and each fiscal year thereafter. Such programs, administered by the Department of Labor, provide job training, counseling, and job placement services for certain veterans, including veterans who are homeless or transitioning from being incarcerated.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr3558"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3558ih.xml"
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
      "title": "Veteran Jobs Training Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran Jobs Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to increase the authorization of appropriations for homeless veterans reintegration programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:36Z"
    }
  ]
}
```
