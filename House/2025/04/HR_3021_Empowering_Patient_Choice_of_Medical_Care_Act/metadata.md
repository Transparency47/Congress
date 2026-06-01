# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3021
- Title: Empowering Patient Choice of Medical Care Act
- Congress: 119
- Bill type: HR
- Bill number: 3021
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-05-21T20:38:22Z
- Update date including text: 2025-05-21T20:38:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3021",
    "number": "3021",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000929",
        "district": "5",
        "firstName": "Victoria",
        "fullName": "Rep. Spartz, Victoria [R-IN-5]",
        "lastName": "Spartz",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Empowering Patient Choice of Medical Care Act",
    "type": "HR",
    "updateDate": "2025-05-21T20:38:22Z",
    "updateDateIncludingText": "2025-05-21T20:38:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-24T15:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3021ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3021\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mrs. Spartz introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo eliminate the inpatient-only service list.\n#### 1. Short title\nThis Act may be cited as the Empowering Patient Choice of Medical Care Act .\n#### 2. Elimination of inpatient-only service list\nBeginning January 1, 2026, the Secretary of Health and Human Services may not refuse to designate an outpatient hospital service pursuant to section 1833(t)(1)(B)(i) of the Social Security Act ( 42 U.S.C. 1395l(t)(1)(B)(i) ) based solely on a determination by the Secretary that such service may only be safely furnished in an inpatient setting.",
      "versionDate": "2025-04-24",
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
        "name": "Health",
        "updateDate": "2025-05-21T10:47:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-24",
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
          "measure-id": "id119hr3021",
          "measure-number": "3021",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-24",
          "originChamber": "HOUSE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3021v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-04-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Empowering Patient Choice of Medical Care Act</b></p> <p>This bill prohibits the Centers for Medicare & Medicaid Services from refusing to designate a service as a covered hospital outpatient service under Medicare based solely on its determination that the service can only be furnished in an inpatient setting.</p>"
        },
        "title": "Empowering Patient Choice of Medical Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3021.xml",
    "summary": {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Empowering Patient Choice of Medical Care Act</b></p> <p>This bill prohibits the Centers for Medicare & Medicaid Services from refusing to designate a service as a covered hospital outpatient service under Medicare based solely on its determination that the service can only be furnished in an inpatient setting.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr3021"
    },
    "title": "Empowering Patient Choice of Medical Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Empowering Patient Choice of Medical Care Act</b></p> <p>This bill prohibits the Centers for Medicare & Medicaid Services from refusing to designate a service as a covered hospital outpatient service under Medicare based solely on its determination that the service can only be furnished in an inpatient setting.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr3021"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3021ih.xml"
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
      "title": "Empowering Patient Choice of Medical Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empowering Patient Choice of Medical Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To eliminate the inpatient-only service list.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:28Z"
    }
  ]
}
```
