# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/830?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/830
- Title: Providing for consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.
- Congress: 119
- Bill type: HRES
- Bill number: 830
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-03-17T15:54:34Z
- Update date including text: 2026-03-17T15:54:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Rules.
- 2025-10-24 - IntroReferral: Submitted in House
- 2025-10-24 - IntroReferral: Submitted in House
- Latest action: 2025-10-24: Submitted in House

## Actions

- 2025-10-24 - IntroReferral: Referred to the House Committee on Rules.
- 2025-10-24 - IntroReferral: Submitted in House
- 2025-10-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/830",
    "number": "830",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000468",
        "district": "7",
        "firstName": "Lizzie",
        "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
        "lastName": "Fletcher",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.",
    "type": "HRES",
    "updateDate": "2026-03-17T15:54:34Z",
    "updateDateIncludingText": "2026-03-17T15:54:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:02:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres830ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 830\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mrs. Fletcher submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 999) to protect an individual\u2019s ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 999) to protect an individual\u2019s ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception. All points of order against consideration of the bill are waived. The bill shall be considered as read. All points of order against provisions in the bill are waived. The previous question shall be considered as ordered on the bill and on any amendment thereto to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Energy and Commerce or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 999.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 999 no later than one week after passage.",
      "versionDate": "2025-10-24",
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
        "updateDate": "2026-01-16T13:26:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-24",
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
          "measure-id": "id119hres830",
          "measure-number": "830",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-24",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres830v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-10-24",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception."
        },
        "title": "Providing for consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres830.xml",
    "summary": {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres830"
    },
    "title": "Providing for consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception."
  },
  "summaries": [
    {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres830"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres830ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T04:18:15Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 999) to protect an individual's ability to access contraceptives and to engage in contraception and to protect a health care providers ability to provide contraceptives, contraception, and information related to contraception.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-25T08:05:44Z"
    }
  ]
}
```
