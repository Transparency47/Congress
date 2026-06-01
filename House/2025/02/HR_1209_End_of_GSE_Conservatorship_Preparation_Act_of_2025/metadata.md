# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1209
- Title: End of GSE Conservatorship Preparation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1209
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-09-26T18:33:00Z
- Update date including text: 2025-09-26T18:33:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1209",
    "number": "1209",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "End of GSE Conservatorship Preparation Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-26T18:33:00Z",
    "updateDateIncludingText": "2025-09-26T18:33:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-11T15:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1209ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1209\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Ogles introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of the Treasury to submit to the Congress completed proposals for the termination of the conservatorships of Fannie Mae and Freddie Mac, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End of GSE Conservatorship Preparation Act of 2025 .\n#### 2. Proposals for termination of conservatorships\n##### (a) Report\nNot later than 30 days after the date of the enactment of this Act, the Secretary of the Treasury shall submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate that identifies whether\u2014\n**(1)**\nthe Department of the Treasury completed the proposal described in article IX of the Letter Agreement to the Amended and Restated Preferred Stock Purchase Agreement between the United States Department of the Treasury and the Federal National Mortgage Association, dated January 14, 2021, and the proposal described in article IX of the Letter Agreement to the Amended and Restated Preferred Stock Purchase Agreement between the United States Department of the Treasury and the Federal Home Loan Mortgage Corporation, dated January 14, 2021; and\n**(2)**\neither or both of such proposals were completed and, if so, includes such completed proposal or proposals.\n##### (b) Proposals\nIf the report required under subsection (a) indicates that either or both of such proposals were not completed, the Secretary of the Treasury shall\u2014\n**(1)**\ninclude in such report the latest incomplete draft or version, if any, of such incomplete proposal or proposals; and\n**(2)**\nnot later than 90 days after the date of the enactment of this Act, complete and submit such proposal or proposals to the committees identified in subsection (a).",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in House"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-12T18:19:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1209",
          "measure-number": "1209",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1209v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>End of GSE Conservatorship Preparation Act of 2025</strong></p><p>This bill requires the Department of the Treasury to report to Congress on the status of proposals to establish a timeline and process (1) to end the conservatorship of Fannie Mae and Freddie Mac by the Federal Housing Finance Agency, and (2) for Treasury to resolve its investment in Fannie Mae and Freddie Mac. (As a result of the financial crisis, Fannie Mae and Freddie Mac entered into a conservatorship in 2008 with the Federal Housing Finance Agency. As part of this agreement, Treasury provided funds to support the solvency of Fannie Mae and Freddie Mac.)\u00a0 \u00a0</p>"
        },
        "title": "End of GSE Conservatorship Preparation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1209.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End of GSE Conservatorship Preparation Act of 2025</strong></p><p>This bill requires the Department of the Treasury to report to Congress on the status of proposals to establish a timeline and process (1) to end the conservatorship of Fannie Mae and Freddie Mac by the Federal Housing Finance Agency, and (2) for Treasury to resolve its investment in Fannie Mae and Freddie Mac. (As a result of the financial crisis, Fannie Mae and Freddie Mac entered into a conservatorship in 2008 with the Federal Housing Finance Agency. As part of this agreement, Treasury provided funds to support the solvency of Fannie Mae and Freddie Mac.)\u00a0 \u00a0</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr1209"
    },
    "title": "End of GSE Conservatorship Preparation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End of GSE Conservatorship Preparation Act of 2025</strong></p><p>This bill requires the Department of the Treasury to report to Congress on the status of proposals to establish a timeline and process (1) to end the conservatorship of Fannie Mae and Freddie Mac by the Federal Housing Finance Agency, and (2) for Treasury to resolve its investment in Fannie Mae and Freddie Mac. (As a result of the financial crisis, Fannie Mae and Freddie Mac entered into a conservatorship in 2008 with the Federal Housing Finance Agency. As part of this agreement, Treasury provided funds to support the solvency of Fannie Mae and Freddie Mac.)\u00a0 \u00a0</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr1209"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1209ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "title": "To require the Secretary of the Treasury to submit to the Congress completed proposals for the termination of the conservatorships of Fannie Mae and Freddie Mac, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T04:48:43Z"
    },
    {
      "title": "End of GSE Conservatorship Preparation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T04:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End of GSE Conservatorship Preparation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T04:38:21Z"
    }
  ]
}
```
