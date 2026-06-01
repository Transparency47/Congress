# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1068?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1068
- Title: Providing for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.
- Congress: 119
- Bill type: HRES
- Bill number: 1068
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-03-17T15:57:33Z
- Update date including text: 2026-03-17T15:57:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Rules.
- 2026-02-20 - IntroReferral: Submitted in House
- 2026-02-20 - IntroReferral: Submitted in House
- Latest action: 2026-02-20: Submitted in House

## Actions

- 2026-02-20 - IntroReferral: Referred to the House Committee on Rules.
- 2026-02-20 - IntroReferral: Submitted in House
- 2026-02-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1068",
    "number": "1068",
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
    "title": "Providing for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.",
    "type": "HRES",
    "updateDate": "2026-03-17T15:57:33Z",
    "updateDateIncludingText": "2026-03-17T15:57:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:32:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1068ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1068\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. McGovern submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies. All points of order against consideration of the joint resolution are waived. An amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the day of consideration of the joint resolution, if submitted by the ranking minority member of the Committee on Rules, shall be considered as adopted. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted. The joint resolution, as amended, shall be considered as read. All points of order against provisions in the joint resolution, as amended, are waived. The previous question shall be considered as ordered on the joint resolution, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the majority leader and minority leader or their respective designees; and (2) one motion to recommit.\n#### 2.\nUpon passage of H.J. Res. 143, an amendment to the title of such joint resolution received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the day of consideration of the joint resolution, if submitted by the ranking minority member of the Committee on Rules, shall be considered as adopted. If more than one such amendment to the title is submitted, then only the last amendment to the title submitted shall be considered as adopted.\n#### 3.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.J. Res. 143.\n#### 4.\nThe Clerk shall transmit to the Senate a message that the House has passed H.J. Res. 143 no later than three calendar days after passage.",
      "versionDate": "2026-02-20",
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
        "updateDate": "2026-03-17T13:21:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-20",
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
          "measure-id": "id119hres1068",
          "measure-number": "1068",
          "measure-type": "hres",
          "orig-publish-date": "2026-02-20",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1068v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2026-02-20",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies."
        },
        "title": "Providing for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1068.xml",
    "summary": {
      "actionDate": "2026-02-20",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres1068"
    },
    "title": "Providing for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies."
  },
  "summaries": [
    {
      "actionDate": "2026-02-20",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres1068"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1068ih.xml"
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
      "title": "Providing for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T09:18:28Z"
    },
    {
      "title": "Providing for consideration of the joint resolution (H.J. Res. 143) enabling Congress to advance important policies.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T09:05:38Z"
    }
  ]
}
```
