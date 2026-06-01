# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5742
- Title: BOPEN Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5742
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-10-20T13:39:18Z
- Update date including text: 2025-10-20T13:39:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5742",
    "number": "5742",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "BOPEN Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-20T13:39:18Z",
    "updateDateIncludingText": "2025-10-20T13:39:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:32:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5742ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5742\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo provide for the payment of staff of the Bureau of Prisons.\n#### 1. Short title\nThis Act may be cited as the Bureau of Prisons Earnings Now Act of 2025 or as the BOPEN Act of 2025 .\n#### 2. Payment of staff of the Bureau of Prisons\n##### (a) In general\nThere are hereby appropriated out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 or fiscal year 2027 are not in effect such sums are necessary for the payment of salaries and expenses of the Bureau of Prisons.\n##### (b) Exception\nSubsection (a) does not apply in the case of any officer of the Bureau of Prisons who is required to be appointed by the President with the advice and consent of the Senate.",
      "versionDate": "2025-10-10",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-10-20T13:30:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-10",
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
          "measure-id": "id119hr5742",
          "measure-number": "5742",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-10",
          "originChamber": "HOUSE",
          "update-date": "2025-10-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5742v00",
            "update-date": "2025-10-20"
          },
          "action-date": "2025-10-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bureau of Prisons Earnings Now Act of 2025 or the\u00a0BOPEN Act of 2025</strong></p><p>This bill provides appropriations for the salaries and expenses of staff of the Bureau of Prisons (BOP) during any period in which interim or full-year appropriations for FY2026 or FY2027 are not in effect (i.e., a government shutdown). The bill does not apply to any officer of the BOP who is required to be appointed by the President with the advice and consent of the Senate.\u00a0</p>"
        },
        "title": "BOPEN Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5742.xml",
    "summary": {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Prisons Earnings Now Act of 2025 or the\u00a0BOPEN Act of 2025</strong></p><p>This bill provides appropriations for the salaries and expenses of staff of the Bureau of Prisons (BOP) during any period in which interim or full-year appropriations for FY2026 or FY2027 are not in effect (i.e., a government shutdown). The bill does not apply to any officer of the BOP who is required to be appointed by the President with the advice and consent of the Senate.\u00a0</p>",
      "updateDate": "2025-10-20",
      "versionCode": "id119hr5742"
    },
    "title": "BOPEN Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Prisons Earnings Now Act of 2025 or the\u00a0BOPEN Act of 2025</strong></p><p>This bill provides appropriations for the salaries and expenses of staff of the Bureau of Prisons (BOP) during any period in which interim or full-year appropriations for FY2026 or FY2027 are not in effect (i.e., a government shutdown). The bill does not apply to any officer of the BOP who is required to be appointed by the President with the advice and consent of the Senate.\u00a0</p>",
      "updateDate": "2025-10-20",
      "versionCode": "id119hr5742"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5742ih.xml"
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
      "title": "BOPEN Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T03:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BOPEN Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Prisons Earnings Now Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the payment of staff of the Bureau of Prisons.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:21Z"
    }
  ]
}
```
