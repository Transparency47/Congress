# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/770
- Title: Accountability for Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 770
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-04-03T19:58:38Z
- Update date including text: 2025-04-03T19:58:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/770",
    "number": "770",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Accountability for Veterans Act",
    "type": "HR",
    "updateDate": "2025-04-03T19:58:38Z",
    "updateDateIncludingText": "2025-04-03T19:58:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr770ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 770\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to report on certain appeals, resources, and health care systems of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Accountability for Veterans Act .\n#### 2. Report on certain appeals, resources, and health care systems of the Department of Veterans Affairs\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on\u2014\n**(1)**\nreasons why there is a backlog of appeals of claims for disability benefits under laws administered by the Secretary;\n**(2)**\nways to increase the amount of information, resources, and tools provided by the Secretary to members of the Armed Forces and spouses of such members participating in the Transition Assistance Program under sections 1142 and 1144 of title 10, United States Code; and\n**(3)**\nthe persistent management problems impacting 1-star health care systems of the Department of Veterans Affairs.",
      "versionDate": "2025-01-28",
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
            "name": "Administrative remedies",
            "updateDate": "2025-03-27T15:27:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-27T15:27:32Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-03-27T15:27:47Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-27T15:27:51Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-27T15:27:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T20:30:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr770",
          "measure-number": "770",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr770v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Accountability for Veterans Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to report to Congress on certain appeals, resources, and VA health care systems. Specifically, the report must address (1) the reasons why there is a backlog of appeals of claims for VA disability benefits; (2) ways to increase the amount of information, resources, and tools provided by the VA to individuals participating in the Transition Assistance Program of the Department of Defense; and (3) the management problems impacting one-star health care systems of the VA.</p>"
        },
        "title": "Accountability for Veterans Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr770.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Accountability for Veterans Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to report to Congress on certain appeals, resources, and VA health care systems. Specifically, the report must address (1) the reasons why there is a backlog of appeals of claims for VA disability benefits; (2) ways to increase the amount of information, resources, and tools provided by the VA to individuals participating in the Transition Assistance Program of the Department of Defense; and (3) the management problems impacting one-star health care systems of the VA.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr770"
    },
    "title": "Accountability for Veterans Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Accountability for Veterans Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to report to Congress on certain appeals, resources, and VA health care systems. Specifically, the report must address (1) the reasons why there is a backlog of appeals of claims for VA disability benefits; (2) ways to increase the amount of information, resources, and tools provided by the VA to individuals participating in the Transition Assistance Program of the Department of Defense; and (3) the management problems impacting one-star health care systems of the VA.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr770"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr770ih.xml"
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
      "title": "Accountability for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accountability for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to report on certain appeals, resources, and health care systems of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:25Z"
    }
  ]
}
```
