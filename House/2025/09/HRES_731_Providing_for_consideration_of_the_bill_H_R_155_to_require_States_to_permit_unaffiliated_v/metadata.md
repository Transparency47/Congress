# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/731?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/731
- Title: Providing for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 731
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-03-17T15:53:54Z
- Update date including text: 2026-03-17T15:53:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Rules.
- 2025-09-17 - IntroReferral: Submitted in House
- 2025-09-17 - IntroReferral: Submitted in House
- Latest action: 2025-09-17: Submitted in House

## Actions

- 2025-09-17 - IntroReferral: Referred to the House Committee on Rules.
- 2025-09-17 - IntroReferral: Submitted in House
- 2025-09-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/731",
    "number": "731",
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
    "title": "Providing for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-03-17T15:53:54Z",
    "updateDateIncludingText": "2026-03-17T15:53:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:04:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres731ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 731\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. Fitzpatrick submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 3 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by Representative Fitzpatrick of Pennsylvania or a designee and an opponent; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H.R. 155.\n#### 3.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is an amendment in the nature of a substitute received for printing in the portion of the Congressional Record designated for that purpose in clause 8 of rule XVIII dated at least one day before the consideration of H.R. 155, if submitted by Representative Fitzpatrick of Pennsylvania. If more than one such amendment is submitted, then only the last amendment submitted shall be considered as adopted.",
      "versionDate": "2025-09-17",
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
        "updateDate": "2026-01-16T13:23:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-17",
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
          "measure-id": "id119hres731",
          "measure-number": "731",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-17",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres731v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-09-17",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes."
        },
        "title": "Providing for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres731.xml",
    "summary": {
      "actionDate": "2025-09-17",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres731"
    },
    "title": "Providing for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-09-17",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres731"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres731ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T08:48:17Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 155) to require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T08:07:14Z"
    }
  ]
}
```
