# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/154?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/154
- Title: Colorado River Basin System Conservation Extension Act
- Congress: 119
- Bill type: S
- Bill number: 154
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-06-18 - Floor: Passed Senate without amendment by Voice Vote. (text: CR S3459)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-06-18 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:21 - Floor: Received in the House.
- 2025-06-23 15:28:39 - Floor: Held at the desk.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-06-18 - Floor: Passed Senate without amendment by Voice Vote. (text: CR S3459)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-06-18 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:21 - Floor: Received in the House.
- 2025-06-23 15:28:39 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/154",
    "number": "154",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Colorado River Basin System Conservation Extension Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-06-23",
      "actionTime": "15:28:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-06-23",
      "actionTime": "15:19:21",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Voice Vote. (text: CR S3459)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-21",
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
        "item": [
          {
            "date": "2025-06-18T17:23:05Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-21T16:27:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "UT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WY"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s154is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 154\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Hickenlooper (for himself, Mr. Barrasso , Mr. Curtis , Ms. Lummis , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Energy and Water Development and Related Agencies Appropriations Act, 2015, to reauthorize the Colorado River System conservation pilot program.\n#### 1. Short title\nThis Act may be cited as the Colorado River Basin System Conservation Extension Act .\n#### 2. Reauthorization of Colorado River System conservation pilot program\nSection 206 of the Energy and Water Development and Related Agencies Appropriations Act, 2015 ( 43 U.S.C. 620 note; Public Law 113\u2013235 ), is amended\u2014\n**(1)**\nin subsection (b)(2), by striking this Act and inserting the Colorado River Basin System Conservation Extension Act ;\n**(2)**\nin subsection (c)(2), by striking 2024 and inserting 2026 ; and\n**(3)**\nin subsection (d), by striking 2025 and inserting 2027 .",
      "versionDate": "2025-01-21",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s154es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 154\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Energy and Water Development and Related Agencies Appropriations Act, 2015, to reauthorize the Colorado River System conservation pilot program.\n#### 1. Short title\nThis Act may be cited as the Colorado River Basin System Conservation Extension Act .\n#### 2. Reauthorization of Colorado River System conservation pilot program\nSection 206 of the Energy and Water Development and Related Agencies Appropriations Act, 2015 ( 43 U.S.C. 620 note; Public Law 113\u2013235 ), is amended\u2014\n**(1)**\nin subsection (b)(2), by striking this Act and inserting the Colorado River Basin System Conservation Extension Act ;\n**(2)**\nin subsection (c)(2), by striking 2024 and inserting 2026 ; and\n**(3)**\nin subsection (d), by striking 2025 and inserting 2027 .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-02-12",
        "text": "Ordered to be Reported (Amended) by Unanimous Consent."
      },
      "number": "231",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Colorado River Basin System Conservation Extension Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Arizona",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "California",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2025-02-28T15:27:51Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-02-28T15:27:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-05-02T13:41:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s154",
          "measure-number": "154",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s154v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Colorado River Basin System Conservation Extension Act</strong></p><p>This bill extends through FY2026 the Bureau of Reclamation's pilot projects\u00a0to increase water levels in the Upper Colorado River Basin and Lake Mead due to drought conditions.</p>"
        },
        "title": "Colorado River Basin System Conservation Extension Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s154.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Colorado River Basin System Conservation Extension Act</strong></p><p>This bill extends through FY2026 the Bureau of Reclamation's pilot projects\u00a0to increase water levels in the Upper Colorado River Basin and Lake Mead due to drought conditions.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s154"
    },
    "title": "Colorado River Basin System Conservation Extension Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Colorado River Basin System Conservation Extension Act</strong></p><p>This bill extends through FY2026 the Bureau of Reclamation's pilot projects\u00a0to increase water levels in the Upper Colorado River Basin and Lake Mead due to drought conditions.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s154"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s154is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s154es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Colorado River Basin System Conservation Extension Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T11:03:17Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Colorado River Basin System Conservation Extension Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Colorado River Basin System Conservation Extension Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy and Water Development and Related Agencies Appropriations Act, 2015, to reauthorize the Colorado River System conservation pilot program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:33:26Z"
    }
  ]
}
```
