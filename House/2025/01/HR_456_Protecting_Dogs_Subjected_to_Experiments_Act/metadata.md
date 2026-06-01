# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/456
- Title: Protecting Dogs Subjected to Experiments Act
- Congress: 119
- Bill type: HR
- Bill number: 456
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-03-19T19:57:52Z
- Update date including text: 2025-03-19T19:57:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/456",
    "number": "456",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Protecting Dogs Subjected to Experiments Act",
    "type": "HR",
    "updateDate": "2025-03-19T19:57:52Z",
    "updateDateIncludingText": "2025-03-19T19:57:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:05:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr456ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 456\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the provision of Federal funds to the National Institutes of Health for the purposes of conducting biological, medical, or behavioral research involving the testing of dogs.\n#### 1. Short title\nThis Act may be cited as the Protecting Dogs Subjected to Experiments Act .\n#### 2. Prohibition on use of Federal funds by National Institutes of Health for certain research involving the testing of dogs\nNo Federal funds made available to the National Institutes of Health may be used for the purposes of conducting biological, medical, or behavioral research involving the testing of dogs.",
      "versionDate": "2025-01-15",
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-02-19T21:21:07Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-02-19T21:21:07Z"
          },
          {
            "name": "Medical ethics",
            "updateDate": "2025-02-19T21:21:07Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-02-19T21:21:07Z"
          },
          {
            "name": "National Institutes of Health (NIH)",
            "updateDate": "2025-02-19T21:21:07Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-02-19T21:21:07Z"
          },
          {
            "name": "Research ethics",
            "updateDate": "2025-02-19T21:21:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-14T15:25:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr456",
          "measure-number": "456",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr456v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Dogs Subjected to Experiments Act</strong></p> <p>This bill prohibits the National Institutes of Health from funding biological, medical, or behavioral research that involves testing dogs.</p>"
        },
        "title": "Protecting Dogs Subjected to Experiments Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr456.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Dogs Subjected to Experiments Act</strong></p> <p>This bill prohibits the National Institutes of Health from funding biological, medical, or behavioral research that involves testing dogs.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr456"
    },
    "title": "Protecting Dogs Subjected to Experiments Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Dogs Subjected to Experiments Act</strong></p> <p>This bill prohibits the National Institutes of Health from funding biological, medical, or behavioral research that involves testing dogs.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr456"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr456ih.xml"
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
      "title": "Protecting Dogs Subjected to Experiments Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Dogs Subjected to Experiments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the provision of Federal funds to the National Institutes of Health for the purposes of conducting biological, medical, or behavioral research involving the testing of dogs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T04:18:24Z"
    }
  ]
}
```
