# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/49?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/49
- Title: No Pro-Abortion Task Force Act
- Congress: 119
- Bill type: HR
- Bill number: 49
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-06T16:49:19Z
- Update date including text: 2025-03-06T16:49:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/49",
    "number": "49",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "No Pro-Abortion Task Force Act",
    "type": "HR",
    "updateDate": "2025-03-06T16:49:19Z",
    "updateDateIncludingText": "2025-03-06T16:49:19Z"
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
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
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
          "date": "2025-01-03T16:11:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr49ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 49\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the use of Federal funds for the HHS Reproductive Healthcare Access Task Force.\n#### 1. Short title\nThis Act may be cited as the No Pro-Abortion Task Force Act .\n#### 2. Prohibition against use of Federal funds for HHS Reproductive Healthcare Access Task Force\nNo Federal funds may be used for\u2014\n**(1)**\nthe HHS Reproductive Healthcare Access Task Force, announced by the Secretary of Health and Human Services on January 21, 2022; or\n**(2)**\nany successor or substantially similar task force.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-02-05T20:58:28Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-02-05T20:58:28Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-05T20:58:28Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-02-05T20:58:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-03T15:03:41Z"
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
          "measure-id": "id119hr49",
          "measure-number": "49",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr49v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Pro-Abortion Task Force Act</strong></p><p>This bill prohibits the use of federal funding for the Department of Health and Human Services (HHS) Reproductive Healthcare Access Task Force or any successor or substantially similar task force.</p><p>HHS launched the task force on January 21, 2022, to identify and coordinate departmental activities related to accessing sexual and reproductive health care.</p>"
        },
        "title": "No Pro-Abortion Task Force Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr49.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Pro-Abortion Task Force Act</strong></p><p>This bill prohibits the use of federal funding for the Department of Health and Human Services (HHS) Reproductive Healthcare Access Task Force or any successor or substantially similar task force.</p><p>HHS launched the task force on January 21, 2022, to identify and coordinate departmental activities related to accessing sexual and reproductive health care.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr49"
    },
    "title": "No Pro-Abortion Task Force Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Pro-Abortion Task Force Act</strong></p><p>This bill prohibits the use of federal funding for the Department of Health and Human Services (HHS) Reproductive Healthcare Access Task Force or any successor or substantially similar task force.</p><p>HHS launched the task force on January 21, 2022, to identify and coordinate departmental activities related to accessing sexual and reproductive health care.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr49"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr49ih.xml"
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
      "title": "No Pro-Abortion Task Force Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T11:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Pro-Abortion Task Force Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds for the HHS Reproductive Healthcare Access Task Force.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T11:03:34Z"
    }
  ]
}
```
