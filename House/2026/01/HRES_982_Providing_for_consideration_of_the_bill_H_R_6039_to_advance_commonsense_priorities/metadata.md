# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/982?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/982
- Title: Providing for consideration of the bill (H.R. 6039) to advance commonsense priorities.
- Congress: 119
- Bill type: HRES
- Bill number: 982
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-01-22T16:16:30Z
- Update date including text: 2026-01-22T16:16:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Rules.
- 2026-01-08 - IntroReferral: Submitted in House
- 2026-01-08 - IntroReferral: Submitted in House
- 2026-01-21 - Discharge: Motion to Discharge Committee filed by Mr. Morelle. Petition No: 119-14. (<a href="https://clerk.house.gov/DischargePetition/2026012114">Discharge petition</a> text with signatures.)
- Latest action: 2026-01-08: Submitted in House

## Actions

- 2026-01-08 - IntroReferral: Referred to the House Committee on Rules.
- 2026-01-08 - IntroReferral: Submitted in House
- 2026-01-08 - IntroReferral: Submitted in House
- 2026-01-21 - Discharge: Motion to Discharge Committee filed by Mr. Morelle. Petition No: 119-14. (<a href="https://clerk.house.gov/DischargePetition/2026012114">Discharge petition</a> text with signatures.)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/982",
    "number": "982",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 6039) to advance commonsense priorities.",
    "type": "HRES",
    "updateDate": "2026-01-22T16:16:30Z",
    "updateDateIncludingText": "2026-01-22T16:16:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H17000",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Morelle. Petition No: 119-14. (<a href=\"https://clerk.house.gov/DischargePetition/2026012114\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T15:03:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres982ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 982\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Mr. Morelle submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 6039) to advance commonsense priorities.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 6039) to advance commonsense priorities. All points of order against consideration of the bill are waived. An amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the day of consideration of H.R. 6039, if submitted by the ranking minority member of the Committee on House Administration, shall be considered as adopted. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on House Administration or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 6039.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 6039 no later than three calendar days after passage.",
      "versionDate": "2026-01-08",
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
        "updateDate": "2026-01-12T14:29:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-08",
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
          "measure-id": "id119hres982",
          "measure-number": "982",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-08",
          "originChamber": "HOUSE",
          "update-date": "2026-01-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres982v00",
            "update-date": "2026-01-09"
          },
          "action-date": "2026-01-08",
          "action-desc": "Introduced in House",
          "summary-text": "Sets forth the rule for consideration of the bill (H.R. 6039) to advance commonsense priorities."
        },
        "title": "Providing for consideration of the bill (H.R. 6039) to advance commonsense priorities."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres982.xml",
    "summary": {
      "actionDate": "2026-01-08",
      "actionDesc": "Introduced in House",
      "text": "Sets forth the rule for consideration of the bill (H.R. 6039) to advance commonsense priorities.",
      "updateDate": "2026-01-09",
      "versionCode": "id119hres982"
    },
    "title": "Providing for consideration of the bill (H.R. 6039) to advance commonsense priorities."
  },
  "summaries": [
    {
      "actionDate": "2026-01-08",
      "actionDesc": "Introduced in House",
      "text": "Sets forth the rule for consideration of the bill (H.R. 6039) to advance commonsense priorities.",
      "updateDate": "2026-01-09",
      "versionCode": "id119hres982"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres982ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 6039) to advance commonsense priorities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:26Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 6039) to advance commonsense priorities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T09:07:09Z"
    }
  ]
}
```
