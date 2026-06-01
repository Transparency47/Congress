# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1096?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1096
- Title: Providing for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 1096
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-05-23T21:06:21Z
- Update date including text: 2026-05-23T21:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Rules.
- 2026-03-03 - IntroReferral: Submitted in House
- 2026-03-03 - IntroReferral: Submitted in House
- 2026-03-18 - Discharge: Motion to Discharge Committee filed by Ms. DeLauro. Petition No: 119-17. (<a href="https://clerk.house.gov/DischargePetition/2026031817">Discharge petition</a> text with signatures.)
- Latest action: 2026-03-03: Submitted in House

## Actions

- 2026-03-03 - IntroReferral: Referred to the House Committee on Rules.
- 2026-03-03 - IntroReferral: Submitted in House
- 2026-03-03 - IntroReferral: Submitted in House
- 2026-03-18 - Discharge: Motion to Discharge Committee filed by Ms. DeLauro. Petition No: 119-17. (<a href="https://clerk.house.gov/DischargePetition/2026031817">Discharge petition</a> text with signatures.)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1096",
    "number": "1096",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-05-23T21:06:21Z",
    "updateDateIncludingText": "2026-05-23T21:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H17000",
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Ms. DeLauro. Petition No: 119-17. (<a href=\"https://clerk.house.gov/DischargePetition/2026031817\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:02:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1096ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1096\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Ms. DeLauro submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes. All points of order against consideration of the bill are waived. An amendment in the nature of a substitute consisting of the text of H.R. 7481, as introduced, shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Appropriations or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 4213.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 4213 no later than three calendar days after passage",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-17T13:21:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-03",
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
          "measure-id": "id119hres1096",
          "measure-number": "1096",
          "measure-type": "hres",
          "orig-publish-date": "2026-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1096v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2026-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes."
        },
        "title": "Providing for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1096.xml",
    "summary": {
      "actionDate": "2026-03-03",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres1096"
    },
    "title": "Providing for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2026-03-03",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres1096"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1096ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-04T09:18:50Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 4213) making appropriations for the Department of Homeland Security for the fiscal year ending September 30, 2026, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-04T09:06:06Z"
    }
  ]
}
```
