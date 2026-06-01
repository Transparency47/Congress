# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/545
- Title: To direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 545
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-03-11T16:15:35Z
- Update date including text: 2025-03-11T16:15:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/545",
    "number": "545",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-03-11T16:15:35Z",
    "updateDateIncludingText": "2025-03-11T16:15:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:09:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr545ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 545\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes.\n#### 1. Study on extreme risk protection orders\nNot later than one year after the date of enactment of this Act, the Attorney General, acting through the Director of the Bureau of Justice Assistance, shall conduct a study on the efficacy of extreme risk protection orders on reducing gun violence.",
      "versionDate": "2025-01-16",
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
            "name": "Crime prevention",
            "updateDate": "2025-02-19T21:24:35Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-02-19T21:24:35Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-19T21:24:35Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-02-19T21:24:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-15T16:05:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr545",
          "measure-number": "545",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr545v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill directs the Bureau of Justice Assistance within the Department of Justice to study the efficacy of extreme risk protection orders on reducing gun violence. </p>"
        },
        "title": "To direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr545.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the Bureau of Justice Assistance within the Department of Justice to study the efficacy of extreme risk protection orders on reducing gun violence. </p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr545"
    },
    "title": "To direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the Bureau of Justice Assistance within the Department of Justice to study the efficacy of extreme risk protection orders on reducing gun violence. </p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr545"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr545ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T13:33:27Z"
    },
    {
      "title": "To direct the Attorney General to conduct a study on the efficacy of extreme risk protection orders on reducing gun violence, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:29Z"
    }
  ]
}
```
