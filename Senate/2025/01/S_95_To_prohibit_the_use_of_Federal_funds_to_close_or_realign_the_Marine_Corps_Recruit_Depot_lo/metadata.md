# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/95?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/95
- Title: Parris Island Protection Act
- Congress: 119
- Bill type: S
- Bill number: 95
- Origin chamber: Senate
- Introduced date: 2025-01-15
- Update date: 2025-12-05T21:51:02Z
- Update date including text: 2025-12-05T21:51:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in Senate
- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-01-15: Introduced in Senate

## Actions

- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/95",
    "number": "95",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Parris Island Protection Act",
    "type": "S",
    "updateDate": "2025-12-05T21:51:02Z",
    "updateDateIncludingText": "2025-12-05T21:51:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T17:41:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s95is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 95\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Mr. Graham (for himself and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo prohibit the use of Federal funds to close or realign the Marine Corps Recruit Depot located at Parris Island, South Carolina.\n#### 1. Short title\nThis Act may be cited as the Parris Island Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Marine Corps Recruit Depot located at Parris Island, South Carolina (in this section referred to as Parris Island ), has served the United States as a home to the Marine Corps since 1891.\n**(2)**\nParris Island stands as a site of cultural and historical significance to the Marine Corps and the fighting spirit of the United States.\n**(3)**\nParris Island offers various and challenging conditions that have prepared members of the Marine Corps for every major conflict since World War I.\n**(4)**\nParris Island has cultivated a legacy of excellence and faithful service to the United States.\n**(5)**\nParris Island is and shall remain the physical home of the Eastern Recruiting Region of the Marine Corps.\n**(6)**\nContinued investments are needed to ensure that Parris Island continues to serve the United States for years to come.\n#### 3. Prohibition of closing or realignment of Marine Corps Recruit Depot located at Parris Island, South Carolina\nNo Federal funds may be used to close or realign Marine Corps Recruit Depot, Parris Island, South Carolina, or to conduct any planning or other activity related to such closure or realignment.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-01-15",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "443",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Parris Island Protection Act",
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
            "name": "Military facilities and property",
            "updateDate": "2025-03-06T16:52:20Z"
          },
          {
            "name": "South Carolina",
            "updateDate": "2025-03-06T16:52:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-21T12:46:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119s95",
          "measure-number": "95",
          "measure-type": "s",
          "orig-publish-date": "2025-01-15",
          "originChamber": "SENATE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s95v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Parris Island Protection Act</strong></p><p>This bill prohibits the use of federal funds to close or realign Marine Corps Recruit Depot, Parris Island in South Carolina, or to conduct any planning or other activity related to such closure or realignment.</p>"
        },
        "title": "Parris Island Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s95.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Parris Island Protection Act</strong></p><p>This bill prohibits the use of federal funds to close or realign Marine Corps Recruit Depot, Parris Island in South Carolina, or to conduct any planning or other activity related to such closure or realignment.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s95"
    },
    "title": "Parris Island Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Parris Island Protection Act</strong></p><p>This bill prohibits the use of federal funds to close or realign Marine Corps Recruit Depot, Parris Island in South Carolina, or to conduct any planning or other activity related to such closure or realignment.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s95"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s95is.xml"
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
      "title": "Parris Island Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Parris Island Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of Federal funds to close or realign the Marine Corps Recruit Depot located at Parris Island, South Carolina.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:35Z"
    }
  ]
}
```
