# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1179?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1179
- Title: Las Cruces Bataan Memorial Clinic Act
- Congress: 119
- Bill type: S
- Bill number: 1179
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-07-01T14:04:19Z
- Update date including text: 2025-07-01T14:04:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1179",
    "number": "1179",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Las Cruces Bataan Memorial Clinic Act",
    "type": "S",
    "updateDate": "2025-07-01T14:04:19Z",
    "updateDateIncludingText": "2025-07-01T14:04:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T17:02:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1179is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1179\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Heinrich introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo name the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, the Las Cruces Bataan Memorial Clinic .\n#### 1. Short title\nThis Act may be cited as the Las Cruces Bataan Memorial Clinic Act .\n#### 2. Name of Department of Veterans Affairs community-based outpatient clinic in Las Cruces, New Mexico\n##### (a) Name\nThe community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, shall after the date of the enactment of this Act be known and designated as the Las Cruces Bataan Memorial Clinic .\n##### (b) Reference\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the clinic referred to in subsection (a) shall be considered to be a reference to the Las Cruces Bataan Memorial Clinic.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "1964",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Las Cruces Bataan Memorial Clinic Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-19T16:14:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119s1179",
          "measure-number": "1179",
          "measure-type": "s",
          "orig-publish-date": "2025-03-27",
          "originChamber": "SENATE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1179v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Las Cruces Bataan Memorial Clinic Act</strong></p><p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, as the Las Cruces Bataan Memorial Clinic.</p>"
        },
        "title": "Las Cruces Bataan Memorial Clinic Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1179.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Las Cruces Bataan Memorial Clinic Act</strong></p><p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, as the Las Cruces Bataan Memorial Clinic.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119s1179"
    },
    "title": "Las Cruces Bataan Memorial Clinic Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Las Cruces Bataan Memorial Clinic Act</strong></p><p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, as the Las Cruces Bataan Memorial Clinic.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119s1179"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1179is.xml"
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
      "title": "Las Cruces Bataan Memorial Clinic Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Las Cruces Bataan Memorial Clinic Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to name the community-based outpatient clinic of the Department of Veterans Affairs in Las Cruces, New Mexico, the \"Las Cruces Bataan Memorial Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:26Z"
    }
  ]
}
```
