# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/999?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/999
- Title: Providing for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.
- Congress: 119
- Bill type: HRES
- Bill number: 999
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-04-03T22:15:42Z
- Update date including text: 2026-04-03T22:15:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Rules.
- 2026-01-14 - IntroReferral: Submitted in House
- 2026-01-14 - IntroReferral: Submitted in House
- Latest action: 2026-01-14: Submitted in House

## Actions

- 2026-01-14 - IntroReferral: Referred to the House Committee on Rules.
- 2026-01-14 - IntroReferral: Submitted in House
- 2026-01-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/999",
    "number": "999",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Providing for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.",
    "type": "HRES",
    "updateDate": "2026-04-03T22:15:42Z",
    "updateDateIncludingText": "2026-04-03T22:15:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:02:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres999ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 999\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. McGovern submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.\nThat immediately upon adoption of this resolution, without intervention of any point of order, the House shall proceed to the consideration in the House of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership. An amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the day of consideration of H. Res. 997, if submitted by the ranking minority member of the Committee on Rules, shall be considered as adopted. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted. The resolution, as amended, shall be considered as read. The previous question shall be considered as ordered on the resolution, as amended, to adoption without intervening motion or demand for division of the question except one hour of debate equally divided and controlled by the majority leader and minority leader or their respective designees.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H. Res. 997.",
      "versionDate": "2026-01-14",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-01-16T12:57:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-14",
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
          "measure-id": "id119hres999",
          "measure-number": "999",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-14",
          "originChamber": "HOUSE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres999v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2026-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership."
        },
        "title": "Providing for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres999.xml",
    "summary": {
      "actionDate": "2026-01-14",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.",
      "updateDate": "2026-03-26",
      "versionCode": "id119hres999"
    },
    "title": "Providing for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership."
  },
  "summaries": [
    {
      "actionDate": "2026-01-14",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.",
      "updateDate": "2026-03-26",
      "versionCode": "id119hres999"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres999ih.xml"
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
      "title": "Providing for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-15T10:48:20Z"
    },
    {
      "title": "Providing for the consideration of the resolution (H. Res. 997) enabling the House of Representatives to be responsive to its membership.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T09:06:38Z"
    }
  ]
}
```
