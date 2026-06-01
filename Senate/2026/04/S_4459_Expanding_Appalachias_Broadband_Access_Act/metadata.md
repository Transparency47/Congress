# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4459
- Title: Expanding Appalachia’s Broadband Access Act
- Congress: 119
- Bill type: S
- Bill number: 4459
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-26T12:27:18Z
- Update date including text: 2026-05-26T12:27:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4459",
    "number": "4459",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Expanding Appalachia\u2019s Broadband Access Act",
    "type": "S",
    "updateDate": "2026-05-26T12:27:18Z",
    "updateDateIncludingText": "2026-05-26T12:27:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T17:57:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4459is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4459\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Husted (for himself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Comptroller General of the United States to conduct a study on the capability of the Appalachian Regional Commission to include satellites in broadband projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Appalachia\u2019s Broadband Access Act .\n#### 2 GAO study on satellite broadband\n##### (a) In general\nNot later than 1 year after the date of enactment of this section, the Comptroller General of the United States shall conduct, and submit to Congress the results thereof, a study on the capability of the Appalachian Regional Commission to incorporate satellites in broadband projects.\n##### (b) Requirements\nIn conducting the study under subsection (a), the Comptroller General of the United States shall\u2014\n**(1)**\nreview the capacity of satellite broadband services to be used for business purposes;\n**(2)**\nevaluate economic development growth in areas that have used satellite broadband for businesses; and\n**(3)**\nanalyze the cost-effectiveness of implementing broadband via satellites for economic development.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2026-03-25",
        "text": "Received in the Senate and Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2474",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expanding Appalachia\u2019s Broadband Access Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-05-21T15:14:44Z"
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
          "measure-id": "id119s4459",
          "measure-number": "4459",
          "measure-type": "s",
          "orig-publish-date": "2026-04-30",
          "originChamber": "SENATE",
          "update-date": "2026-05-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4459v00",
            "update-date": "2026-05-26"
          },
          "action-date": "2026-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Expanding Appalachia\u2019s Broadband Access Act</strong></p><p>This bill requires the Government Accountability Office to study and report to Congress on the Appalachian Regional Commission\u2019s capability to incorporate satellites in broadband projects. Specifically, the study must review and analyze the capacity and cost-effectiveness of using satellite broadband service for business purposes and economic development.\u00a0</p>"
        },
        "title": "Expanding Appalachia\u2019s Broadband Access Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4459.xml",
    "summary": {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanding Appalachia\u2019s Broadband Access Act</strong></p><p>This bill requires the Government Accountability Office to study and report to Congress on the Appalachian Regional Commission\u2019s capability to incorporate satellites in broadband projects. Specifically, the study must review and analyze the capacity and cost-effectiveness of using satellite broadband service for business purposes and economic development.\u00a0</p>",
      "updateDate": "2026-05-26",
      "versionCode": "id119s4459"
    },
    "title": "Expanding Appalachia\u2019s Broadband Access Act"
  },
  "summaries": [
    {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanding Appalachia\u2019s Broadband Access Act</strong></p><p>This bill requires the Government Accountability Office to study and report to Congress on the Appalachian Regional Commission\u2019s capability to incorporate satellites in broadband projects. Specifically, the study must review and analyze the capacity and cost-effectiveness of using satellite broadband service for business purposes and economic development.\u00a0</p>",
      "updateDate": "2026-05-26",
      "versionCode": "id119s4459"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4459is.xml"
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
      "title": "Expanding Appalachia\u2019s Broadband Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-09T05:23:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanding Appalachia\u2019s Broadband Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Comptroller General of the United States to conduct a study on the capability of the Appalachian Regional Commission to include satellites in broadband projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:34Z"
    }
  ]
}
```
