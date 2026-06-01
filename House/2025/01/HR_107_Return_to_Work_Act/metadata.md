# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/107
- Title: Return to Work Act
- Congress: 119
- Bill type: HR
- Bill number: 107
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-07T15:45:43Z
- Update date including text: 2025-03-07T15:45:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/107",
    "number": "107",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Return to Work Act",
    "type": "HR",
    "updateDate": "2025-03-07T15:45:43Z",
    "updateDateIncludingText": "2025-03-07T15:45:43Z"
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
          "date": "2025-01-03T16:11:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr107ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 107\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require Executive agencies to reinstate telework policies that were in place on December 31, 2019, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Return to Work Act .\n#### 2. Reinstate prior remote work policies\n##### (a) In general\nNot later than 60 days after the date of the enactment of this Act, the head of each Executive agency shall reinstate the telework policies in use by such Executive agency on December 31, 2019.\n##### (b) Rule of construction\nBeginning on the date on which the head of an Executive agency reinstates the telework policies in use by such Executive agency on December 31, 2019, the reinstated telework policy of such Executive agency shall apply in place of any telework provision of a teleworking, collective bargaining, or other employment agreement of such Executive agency to the extent that such telework provision conflicts with, or applies a different telework policy than, the reinstated telework policy of such Executive agency.\n##### (c) Definitions\nIn this section:\n**(1) Executive agency**\nThe term Executive agency has the meaning given such term in section 105 of title 5, United States Code.\n**(2) Reinstated telework policy**\nThe term reinstated telework policy means the telework policies in use by an Executive agency on December 31, 2019.\n**(3) Telework**\nThe term telework has the meaning given such term in section 6501 of title 5, United States Code.",
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
            "name": "Commuting",
            "updateDate": "2025-03-05T15:27:34Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-05T15:27:34Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-05T15:27:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T19:44:59Z"
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
          "measure-id": "id119hr107",
          "measure-number": "107",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr107v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Return to Work Act</b></p> <p>This bill requires the head of each executive agency to reinstate the telework policies in use by that agency on December 31, 2019.</p>"
        },
        "title": "Return to Work Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr107.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Return to Work Act</b></p> <p>This bill requires the head of each executive agency to reinstate the telework policies in use by that agency on December 31, 2019.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr107"
    },
    "title": "Return to Work Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Return to Work Act</b></p> <p>This bill requires the head of each executive agency to reinstate the telework policies in use by that agency on December 31, 2019.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr107"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr107ih.xml"
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
      "title": "Return to Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Return to Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require Executive agencies to reinstate telework policies that were in place on December 31, 2019, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:27Z"
    }
  ]
}
```
