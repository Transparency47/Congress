# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/9?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/9
- Title: Reaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court.
- Congress: 119
- Bill type: HRES
- Bill number: 9
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-16T21:26:51Z
- Update date including text: 2025-01-16T21:26:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/9",
    "number": "9",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "Reaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court.",
    "type": "HRES",
    "updateDate": "2025-01-16T21:26:51Z",
    "updateDateIncludingText": "2025-01-16T21:26:51Z"
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-03T16:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres9ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 9\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nReaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court.\nThat the House of Representatives\u2014\n**(1)**\nreaffirms that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court;\n**(2)**\ncondemns the International Criminal Court\u2019s issuance of arrest warrant applications for Israeli Prime Minister Benjamin Netanyahu and Minister of Defense Yoav Gallant; and\n**(3)**\nreiterates its unwavering support for the State of Israel and its right to defend itself and its leaders from unwarranted international legal actions.",
      "versionDate": "2025-01-03",
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
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-01-15T21:25:12Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-01-15T21:25:45Z"
          },
          {
            "name": "International law and treaties",
            "updateDate": "2025-01-15T21:25:22Z"
          },
          {
            "name": "Israel",
            "updateDate": "2025-01-15T21:25:30Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-01-15T21:25:36Z"
          },
          {
            "name": "Specialized courts",
            "updateDate": "2025-01-15T21:25:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-01-14T16:30:54Z"
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
          "measure-id": "id119hres9",
          "measure-number": "9",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres9v00",
            "update-date": "2025-01-16"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution reaffirms that the United States in not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court (ICC). \u00a0The resolution also (1) condemns the ICC's issuance of arrest warrant applications for Israeli Prime Minister Benjamin Netanyahu and\u00a0Israeli Minister of Defense Yoav Gallant, and (2) supports Israel's right to defend itself and its leaders from unwarranted international legal actions.\u00a0</p>"
        },
        "title": "Reaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres9.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution reaffirms that the United States in not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court (ICC). \u00a0The resolution also (1) condemns the ICC's issuance of arrest warrant applications for Israeli Prime Minister Benjamin Netanyahu and\u00a0Israeli Minister of Defense Yoav Gallant, and (2) supports Israel's right to defend itself and its leaders from unwarranted international legal actions.\u00a0</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hres9"
    },
    "title": "Reaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution reaffirms that the United States in not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court (ICC). \u00a0The resolution also (1) condemns the ICC's issuance of arrest warrant applications for Israeli Prime Minister Benjamin Netanyahu and\u00a0Israeli Minister of Defense Yoav Gallant, and (2) supports Israel's right to defend itself and its leaders from unwarranted international legal actions.\u00a0</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hres9"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres9ih.xml"
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
      "title": "Reaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reaffirming that the United States is not a party to the Rome Statute and does not recognize the jurisdiction of the International Criminal Court.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:27Z"
    }
  ]
}
```
