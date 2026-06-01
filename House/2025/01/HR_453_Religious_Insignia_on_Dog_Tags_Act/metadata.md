# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/453?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/453
- Title: Religious Insignia on Dog Tags Act
- Congress: 119
- Bill type: HR
- Bill number: 453
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-06-06T14:17:56Z
- Update date including text: 2025-06-06T14:17:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/453",
    "number": "453",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Religious Insignia on Dog Tags Act",
    "type": "HR",
    "updateDate": "2025-06-06T14:17:56Z",
    "updateDateIncludingText": "2025-06-06T14:17:56Z"
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
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
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
          "date": "2025-01-15T15:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr453ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 453\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to revise and update the Department of Defense regulations to allow trademarks owned or controlled by the Department of Defense to be combined with religious insignia on commercial identification tags (commonly known as dog tags ) and to be sold by lawful trademark licensees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Religious Insignia on Dog Tags Act .\n#### 2. Religious insignia on commercial identification tags\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall review and update Department of Defense Directive 5535.12 and any associated regulations to allow trademarks owned or controlled by the Department of Defense to be combined with religious insignia on commercial identification tags (commonly known as dog tags ) and to be sold by lawful trademark licensees.\n##### (b) Retroactive effective date\nThe update to the Directive under subsection (a) shall be deemed to have taken effect on September 13, 2013.",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-06T16:52:42Z"
          },
          {
            "name": "Department of Defense",
            "updateDate": "2025-03-06T16:52:42Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-03-06T16:52:42Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-03-06T16:52:42Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-03-06T16:52:42Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-03-06T16:52:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T16:50:51Z"
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
          "measure-id": "id119hr453",
          "measure-number": "453",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr453v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Religious Insignia on Dog Tags Act</b></p> <p>This bill directs the Department of Defense (DOD) to allow trademarks owned or controlled by DOD to be combined with religious insignia on commercial identification tags (i.e., dog tags) and to be sold by lawful trademark licensees.</p> <p>The bill applies retroactively to September 13, 2013. </p>"
        },
        "title": "Religious Insignia on Dog Tags Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr453.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Religious Insignia on Dog Tags Act</b></p> <p>This bill directs the Department of Defense (DOD) to allow trademarks owned or controlled by DOD to be combined with religious insignia on commercial identification tags (i.e., dog tags) and to be sold by lawful trademark licensees.</p> <p>The bill applies retroactively to September 13, 2013. </p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr453"
    },
    "title": "Religious Insignia on Dog Tags Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Religious Insignia on Dog Tags Act</b></p> <p>This bill directs the Department of Defense (DOD) to allow trademarks owned or controlled by DOD to be combined with religious insignia on commercial identification tags (i.e., dog tags) and to be sold by lawful trademark licensees.</p> <p>The bill applies retroactively to September 13, 2013. </p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr453"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr453ih.xml"
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
      "title": "Religious Insignia on Dog Tags Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Religious Insignia on Dog Tags Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to revise and update the Department of Defense regulations to allow trademarks owned or controlled by the Department of Defense to be combined with religious insignia on commercial identification tags (commonly known as \"dog tags\") and to be sold by lawful trademark licensees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T04:18:19Z"
    }
  ]
}
```
