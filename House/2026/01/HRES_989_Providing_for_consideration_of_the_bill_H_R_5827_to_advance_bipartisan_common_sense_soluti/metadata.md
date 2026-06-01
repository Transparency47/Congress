# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/989?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/989
- Title: Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.
- Congress: 119
- Bill type: HRES
- Bill number: 989
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-04-09T14:26:28Z
- Update date including text: 2026-04-09T14:26:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Rules.
- 2026-01-12 - IntroReferral: Submitted in House
- 2026-01-12 - IntroReferral: Submitted in House
- Latest action: 2026-01-12: Submitted in House

## Actions

- 2026-01-12 - IntroReferral: Referred to the House Committee on Rules.
- 2026-01-12 - IntroReferral: Submitted in House
- 2026-01-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/989",
    "number": "989",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.",
    "type": "HRES",
    "updateDate": "2026-04-09T14:26:28Z",
    "updateDateIncludingText": "2026-04-09T14:26:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T17:03:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres989ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 989\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Suozzi submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 5827) to advance bipartisan, common sense solutions. All points of order against consideration of the bill are waived. An amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the day of consideration of H.R. 5827, if submitted by Representative Suozzi of New York, shall be considered as adopted. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by Representative Suozzi of New York and an opponent or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 5827.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 5827 no later than one calendar day after passage.",
      "versionDate": "2026-01-12",
      "versionType": "IH"
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
        "actionDate": "2026-04-02",
        "text": "Referred to the House Committee on Rules."
      },
      "number": "1153",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.",
      "type": "HRES"
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
        "updateDate": "2026-01-16T13:32:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-12",
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
          "measure-id": "id119hres989",
          "measure-number": "989",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-12",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres989v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2026-01-12",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions."
        },
        "title": "Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres989.xml",
    "summary": {
      "actionDate": "2026-01-12",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres989"
    },
    "title": "Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions."
  },
  "summaries": [
    {
      "actionDate": "2026-01-12",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres989"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres989ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T09:18:36Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 5827) to advance bipartisan, common sense solutions.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T09:05:36Z"
    }
  ]
}
```
