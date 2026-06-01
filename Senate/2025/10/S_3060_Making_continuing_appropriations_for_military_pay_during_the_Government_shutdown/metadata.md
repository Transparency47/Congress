# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3060?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3060
- Title: Paychecks for Patriots Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3060
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2025-11-03T15:20:44Z
- Update date including text: 2025-11-03T15:20:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3060",
    "number": "3060",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Paychecks for Patriots Act of 2025",
    "type": "S",
    "updateDate": "2025-11-03T15:20:44Z",
    "updateDateIncludingText": "2025-11-03T15:20:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T16:38:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3060is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3060\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nMaking continuing appropriations for military pay during the Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Paychecks for Patriots Act of 2025 .\n#### 2. Continuing appropriations for members of the Armed Forces\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 are not in effect, such sums as are necessary to provide pay and allowances to members of the Armed Forces, including reserve components thereof, who perform active service or inactive duty training during such period.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until the enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.",
      "versionDate": "2025-10-28",
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
        "actionDate": "2025-10-30",
        "text": "Referred to the Committee on Appropriations by unanimous consent."
      },
      "number": "3002",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Military Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-16",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5401",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Troops Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-30",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5660",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Military Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-30",
        "text": "Read twice and referred to the Committee on Appropriations."
      },
      "number": "3079",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Armed Forces Pay Act of 2025",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-10-30T13:38:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-28",
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
          "measure-id": "id119s3060",
          "measure-number": "3060",
          "measure-type": "s",
          "orig-publish-date": "2025-10-28",
          "originChamber": "SENATE",
          "update-date": "2025-10-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3060v00",
            "update-date": "2025-10-30"
          },
          "action-date": "2025-10-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Paychecks for Patriots Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay during any period in\u00a0which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2026 continuing appropriations for the pay and allowances of members of the Armed Forces, including reserve components, who perform active service or inactive duty training during the period.\u00a0</p><p>The appropriations provided by this bill are available until legislation is enacted that provides FY2026 appropriations for military pay (including continuing appropriations for this purpose).\u00a0</p>"
        },
        "title": "Paychecks for Patriots Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3060.xml",
    "summary": {
      "actionDate": "2025-10-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Paychecks for Patriots Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay during any period in\u00a0which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2026 continuing appropriations for the pay and allowances of members of the Armed Forces, including reserve components, who perform active service or inactive duty training during the period.\u00a0</p><p>The appropriations provided by this bill are available until legislation is enacted that provides FY2026 appropriations for military pay (including continuing appropriations for this purpose).\u00a0</p>",
      "updateDate": "2025-10-30",
      "versionCode": "id119s3060"
    },
    "title": "Paychecks for Patriots Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Paychecks for Patriots Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay during any period in\u00a0which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2026 continuing appropriations for the pay and allowances of members of the Armed Forces, including reserve components, who perform active service or inactive duty training during the period.\u00a0</p><p>The appropriations provided by this bill are available until legislation is enacted that provides FY2026 appropriations for military pay (including continuing appropriations for this purpose).\u00a0</p>",
      "updateDate": "2025-10-30",
      "versionCode": "id119s3060"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3060is.xml"
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
      "title": "Paychecks for Patriots Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Paychecks for Patriots Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill making continuing appropriations for military pay during the Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T03:48:14Z"
    }
  ]
}
```
