# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1029?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1029
- Title: Providing for consideration of the bill (H.R. 6636) to advance sensible priorities.
- Congress: 119
- Bill type: HRES
- Bill number: 1029
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-03-17T15:59:27Z
- Update date including text: 2026-03-17T15:59:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Rules.
- 2026-02-02 - IntroReferral: Submitted in House
- 2026-02-02 - IntroReferral: Submitted in House
- Latest action: 2026-02-02: Submitted in House

## Actions

- 2026-02-02 - IntroReferral: Referred to the House Committee on Rules.
- 2026-02-02 - IntroReferral: Submitted in House
- 2026-02-02 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1029",
    "number": "1029",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 6636) to advance sensible priorities.",
    "type": "HRES",
    "updateDate": "2026-03-17T15:59:27Z",
    "updateDateIncludingText": "2026-03-17T15:59:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
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
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:02:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1029ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1029\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mr. Fitzpatrick submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 6636) to advance sensible priorities.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 6636) to advance sensible priorities. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 3 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by Representative Fitzpatrick of Pennsylvania or a designee and an opponent; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H.R. 6636.\n#### 3.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is an amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the consideration of H.R. 6636, if submitted by Representative Fitzpatrick of Pennsylvania. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted.",
      "versionDate": "2026-02-02",
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
        "updateDate": "2026-03-09T19:06:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-02",
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
          "measure-id": "id119hres1029",
          "measure-number": "1029",
          "measure-type": "hres",
          "orig-publish-date": "2026-02-02",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1029v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2026-02-02",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 6636) to advance sensible priorities."
        },
        "title": "Providing for consideration of the bill (H.R. 6636) to advance sensible priorities."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1029.xml",
    "summary": {
      "actionDate": "2026-02-02",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 6636) to advance sensible priorities.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres1029"
    },
    "title": "Providing for consideration of the bill (H.R. 6636) to advance sensible priorities."
  },
  "summaries": [
    {
      "actionDate": "2026-02-02",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 6636) to advance sensible priorities.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres1029"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1029ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 6636) to advance sensible priorities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:48Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 6636) to advance sensible priorities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T09:05:52Z"
    }
  ]
}
```
