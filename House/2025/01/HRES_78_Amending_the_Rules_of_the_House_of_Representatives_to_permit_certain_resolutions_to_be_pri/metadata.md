# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/78?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/78
- Title: Amending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.
- Congress: 119
- Bill type: HRES
- Bill number: 78
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-03-17T19:41:03Z
- Update date including text: 2025-03-17T19:41:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/78",
    "number": "78",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Amending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.",
    "type": "HRES",
    "updateDate": "2025-03-17T19:41:03Z",
    "updateDateIncludingText": "2025-03-17T19:41:03Z"
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-28T16:07:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres78ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 78\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Williams of Georgia submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.\n#### 1. Limitation on privileged status of certain resolutions\nRule IX of the Rules of the House of Representatives is amended by adding at the end the following:\n3. (a) A resolution described in paragraph (b) shall not raise a question of privilege for purposes of this rule unless\u2014 (1) the committee to whom the resolution is referred has conducted an investigation and filed a report recommending that the House impose the sanction provided by the resolution; or (2) the resolution is offered by direction of a party caucus or conference. (b) A resolution described in this paragraph is\u2014 (1) a resolution impeaching an officer of the Government; or (2) a resolution to censure, reprimand, or expel a Member, Delegate, or Resident Commissioner or to cause a vacancy to occur in the office of the Speaker or in the position of a chair or ranking minority member of a committee. .",
      "versionDate": "2025-01-28",
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
            "name": "Congressional committees",
            "updateDate": "2025-02-28T15:25:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-28T15:25:17Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-02-28T15:25:05Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-02-28T15:24:50Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-28T15:24:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-31T14:27:44Z"
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
          "measure-id": "id119hres78",
          "measure-number": "78",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres78v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution amends the House rules to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.</p><p>This applies to a resolution (1) impeaching an officer of the government; (2) censuring, reprimanding, or expelling a Member, Delegate, or Resident Commissioner; or (3) causing a vacancy to occur in the office of the Speaker or in the position of a chair or ranking minority member of a committee.</p>"
        },
        "title": "Amending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres78.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution amends the House rules to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.</p><p>This applies to a resolution (1) impeaching an officer of the government; (2) censuring, reprimanding, or expelling a Member, Delegate, or Resident Commissioner; or (3) causing a vacancy to occur in the office of the Speaker or in the position of a chair or ranking minority member of a committee.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hres78"
    },
    "title": "Amending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference."
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution amends the House rules to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.</p><p>This applies to a resolution (1) impeaching an officer of the government; (2) censuring, reprimanding, or expelling a Member, Delegate, or Resident Commissioner; or (3) causing a vacancy to occur in the office of the Speaker or in the position of a chair or ranking minority member of a committee.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hres78"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres78ih.xml"
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
      "title": "Amending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:23Z"
    },
    {
      "title": "Amending the Rules of the House of Representatives to permit certain resolutions to be privileged only if they are based on conduct which was the subject of an investigation and report by the appropriate committee of jurisdiction or if they are offered by direction of a party caucus or conference.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T09:06:10Z"
    }
  ]
}
```
