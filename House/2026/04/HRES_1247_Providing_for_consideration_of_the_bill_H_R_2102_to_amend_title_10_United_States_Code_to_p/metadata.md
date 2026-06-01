# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1247
- Title: Providing for consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 1247
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-22T13:54:44Z
- Update date including text: 2026-05-22T13:54:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Rules.
- 2026-04-30 - IntroReferral: Submitted in House
- 2026-05-21 - Discharge: Motion to Discharge Committee filed by Mr. Takano. Petition No: 119-22. (<a href="https://clerk.house.gov/DischargePetition/2026052122">Discharge petition</a> text with signatures.)
- Latest action: 2026-04-30: Submitted in House

## Actions

- 2026-04-30 - IntroReferral: Referred to the House Committee on Rules.
- 2026-04-30 - IntroReferral: Submitted in House
- 2026-05-21 - Discharge: Motion to Discharge Committee filed by Mr. Takano. Petition No: 119-22. (<a href="https://clerk.house.gov/DischargePetition/2026052122">Discharge petition</a> text with signatures.)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1247",
    "number": "1247",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-05-22T13:54:44Z",
    "updateDateIncludingText": "2026-05-22T13:54:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H17000",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Takano. Petition No: 119-22. (<a href=\"https://clerk.house.gov/DischargePetition/2026052122\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionCode": "1025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
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
          "date": "2026-04-30T13:05:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1247ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1247\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Takano (for himself and Mr. Ruiz ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans\u2019 disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans\u2019 disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 4 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided among and controlled by the chair and ranking minority member of the Committee on Armed Services or their respective designees and the chair and ranking minority member of the Committee on Veterans\u2019 Affairs or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 2102.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 2102 no later than three calendar days after passage.\n#### 4.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is as follows:\nStrike all after the enacting clause and insert the following:",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-06T14:25:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-30",
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
          "measure-id": "id119hres1247",
          "measure-number": "1247",
          "measure-type": "hres",
          "orig-publish-date": "2026-04-30",
          "originChamber": "HOUSE",
          "update-date": "2026-05-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1247v00",
            "update-date": "2026-05-04"
          },
          "action-date": "2026-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes."
        },
        "title": "Major Richard Star Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1247.xml",
    "summary": {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.",
      "updateDate": "2026-05-04",
      "versionCode": "id119hres1247"
    },
    "title": "Major Richard Star Act"
  },
  "summaries": [
    {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.",
      "updateDate": "2026-05-04",
      "versionCode": "id119hres1247"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1247ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T17:04:34Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.",
      "titleType": "Override Display Title",
      "titleTypeCode": "81",
      "updateDate": "2026-05-21T17:04:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for consideration of the bill (H.R. 2102) to amend title 10, United States Code, to provide for concurrent receipt of veterans' disability compensation and retired pay for disability retirees with combat-related disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-04T13:33:26Z"
    }
  ]
}
```
