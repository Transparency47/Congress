# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/443?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/443
- Title: Parris Island Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 443
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-02-27T22:41:18Z
- Update date including text: 2026-02-27T22:41:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Armed Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/443",
    "number": "443",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Parris Island Protection Act",
    "type": "HR",
    "updateDate": "2026-02-27T22:41:18Z",
    "updateDateIncludingText": "2026-02-27T22:41:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "SC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "SC"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "SC"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "SC"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr443ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 443\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Mace (for herself, Mr. Wilson of South Carolina , Mrs. Biggs of South Carolina , Mr. Timmons , Mr. Norman , and Mr. Fry ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo prohibit the use of Federal funds to close or realign the Marine Corps Recruit Depot located at Parris Island, South Carolina.\n#### 1. Short title\nThis Act may be cited as the Parris Island Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Marine Corps Recruit Depot located at Parris Island, South Carolina (in this section referred to as Parris Island ), has served the United States as a home to the Marine Corps since 1891.\n**(2)**\nParris Island stands as a site of cultural and historical significance to the Marine Corps and the fighting spirit of the United States.\n**(3)**\nParris Island offers various and challenging conditions that have prepared members of the Marine Corps for every major conflict since World War I.\n**(4)**\nParris Island has cultivated a legacy of excellence and faithful service to the United States.\n**(5)**\nParris Island is and shall remain the physical home of the Eastern Recruiting Region of the Marine Corps.\n**(6)**\nContinued investments are needed to ensure that Parris Island continues to serve the United States for years to come.\n#### 3. Prohibition of closing or realignment of marine corps recruit depot located at Parris Island, South Carolina\nNo Federal funds may be used to close or realign Marine Corps Recruit Depot, Parris Island, South Carolina, or to conduct any planning or other activity related to such closure or realignment.",
      "versionDate": "2025-01-15",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "95",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Parris Island Protection Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Military facilities and property",
            "updateDate": "2025-03-06T16:52:00Z"
          },
          {
            "name": "South Carolina",
            "updateDate": "2025-03-06T16:51:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-21T12:43:21Z"
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
          "measure-id": "id119hr443",
          "measure-number": "443",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr443v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Parris Island Protection Act</strong></p><p>This bill prohibits the use of federal funds to close or realign Marine Corps Recruit Depot, Parris Island in South Carolina, or to conduct any planning or other activity related to such closure or realignment.</p>"
        },
        "title": "Parris Island Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr443.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parris Island Protection Act</strong></p><p>This bill prohibits the use of federal funds to close or realign Marine Corps Recruit Depot, Parris Island in South Carolina, or to conduct any planning or other activity related to such closure or realignment.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr443"
    },
    "title": "Parris Island Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parris Island Protection Act</strong></p><p>This bill prohibits the use of federal funds to close or realign Marine Corps Recruit Depot, Parris Island in South Carolina, or to conduct any planning or other activity related to such closure or realignment.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr443"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr443ih.xml"
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
      "title": "Parris Island Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parris Island Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds to close or realign the Marine Corps Recruit Depot located at Parris Island, South Carolina.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:18Z"
    }
  ]
}
```
