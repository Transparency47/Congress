# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2793?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2793
- Title: Retirement Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 2793
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-12-05T21:38:39Z
- Update date including text: 2025-12-05T21:38:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2793",
    "number": "2793",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000609",
        "district": "6",
        "firstName": "Gary",
        "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
        "lastName": "Palmer",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Retirement Freedom Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:38:39Z",
    "updateDateIncludingText": "2025-12-05T21:38:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:04:25Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2793ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2793\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Palmer introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo allow individuals to choose to opt out of the Medicare part A benefit.\n#### 1. Short title\nThis Act may be cited as the Retirement Freedom Act .\n#### 2. Allowing individuals to choose to opt out of the Medicare part A benefit\nAny individual who is otherwise entitled to benefits under part A of title XVIII of the Social Security Act may elect (in such form and manner as may be specified by the Secretary of Health and Human Services) to opt out of such entitlement. Notwithstanding any other provision of law, in the case of an individual who makes such an election, such individual\u2014\n**(1)**\nmay (in such form and manner as may be specified by the Secretary) subsequently choose to end such election and opt back into such entitlement (in accordance with a process determined by the Secretary) without being subject to any penalty;\n**(2)**\nshall not be required to opt out of benefits under title II of such Act as a condition for making such election; and\n**(3)**\nshall not be required to repay any amount paid under such part A for items and services furnished prior to making such election.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2810",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Retirement Freedom Act",
      "type": "S"
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
        "name": "Health",
        "updateDate": "2025-05-23T14:20:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119hr2793",
          "measure-number": "2793",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-09",
          "originChamber": "HOUSE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2793v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Retirement Freedom Act</strong></p><p>This bill allows an individual to opt out of Medicare hospital services benefits without also having to opt out of Social Security benefits and without having to repay Medicare hospital services benefits already received. The bill also allows an individual to opt back in with no penalty.</p>"
        },
        "title": "Retirement Freedom Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2793.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Retirement Freedom Act</strong></p><p>This bill allows an individual to opt out of Medicare hospital services benefits without also having to opt out of Social Security benefits and without having to repay Medicare hospital services benefits already received. The bill also allows an individual to opt back in with no penalty.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr2793"
    },
    "title": "Retirement Freedom Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Retirement Freedom Act</strong></p><p>This bill allows an individual to opt out of Medicare hospital services benefits without also having to opt out of Social Security benefits and without having to repay Medicare hospital services benefits already received. The bill also allows an individual to opt back in with no penalty.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr2793"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2793ih.xml"
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
      "title": "Retirement Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Retirement Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow individuals to choose to opt out of the Medicare part A benefit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:24Z"
    }
  ]
}
```
