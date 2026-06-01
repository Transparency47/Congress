# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1483
- Title: TSA Commuting Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 1483
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-01-14T16:27:15Z
- Update date including text: 2026-01-14T16:27:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1483",
    "number": "1483",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "TSA Commuting Fairness Act",
    "type": "S",
    "updateDate": "2026-01-14T16:27:15Z",
    "updateDateIncludingText": "2026-01-14T16:27:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-10T21:31:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1483is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1483\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Ms. Duckworth introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo reduce commuting burdens on Transportation Security Administration employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TSA Commuting Fairness Act .\n#### 2. Feasibility study on TSA commuting benefits\n##### (a) In general\nNot later than 270 days after the date of the enactment of this Act, the Administrator of the Transportation Security Administration shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Homeland Security and Governmental Affairs of the Senate a study on the feasibility of treating as on-duty hours the time Transportation Security Administration employees working at airport locations spend traveling between regular duty locations and airport parking lots and bus and transit stops.\n##### (b) Considerations\nIn conducting the feasibility study required under subsection (a), the Administrator of the Transportation Security Administration shall consider the following with respect to Transportation Security Administration employees:\n**(1)**\nThe amount of time needed by such employees to travel between regular duty locations and airport parking lots and bus and transit stops at small hub airports, medium hub airports, and large hub airports (as such terms are defined in section 40102 of title 49, United States Code).\n**(2)**\nThe amount of time such employees spend commuting, on average, exclusive of the time described in paragraph (1).\n**(3)**\nThe potential benefits to such employees and the Administration of treating as on-duty hours the time described in such paragraph.\n**(4)**\nThe feasibility of using mobile phones, location data, and any other means to allow such employees to report their arrival to and departure from the airport parking lots and bus and transit stops concerned.\n**(5)**\nThe estimated costs of treating as on-duty hours the time described in such paragraph, including by considering such hours creditable as basic pay for retirement purposes.\n**(6)**\nOther considerations determined appropriate by the Administrator.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-01-13",
        "actionTime": "18:36:04",
        "text": "House requested return of papers pursuant to H. Res. 991"
      },
      "number": "1834",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Breaking the Gridlock Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "862",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TSA Commuting Fairness Act",
      "type": "HR"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-20T14:24:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
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
          "measure-id": "id119s1483",
          "measure-number": "1483",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1483v00",
            "update-date": "2025-05-22"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>TSA Commuting Fairness Act</strong></p><p>This bill directs the Transportation Security Administration (TSA) to submit to Congress a study on the feasibility of treating as on-duty hours the time TSA employees working at airport locations spend traveling between regular duty locations, airport parking lots,\u00a0and bus and transit stops.</p>"
        },
        "title": "TSA Commuting Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1483.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>TSA Commuting Fairness Act</strong></p><p>This bill directs the Transportation Security Administration (TSA) to submit to Congress a study on the feasibility of treating as on-duty hours the time TSA employees working at airport locations spend traveling between regular duty locations, airport parking lots,\u00a0and bus and transit stops.</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119s1483"
    },
    "title": "TSA Commuting Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>TSA Commuting Fairness Act</strong></p><p>This bill directs the Transportation Security Administration (TSA) to submit to Congress a study on the feasibility of treating as on-duty hours the time TSA employees working at airport locations spend traveling between regular duty locations, airport parking lots,\u00a0and bus and transit stops.</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119s1483"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1483is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "TSA Commuting Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TSA Commuting Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reduce commuting burdens on Transportation Security Administration employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:20Z"
    }
  ]
}
```
