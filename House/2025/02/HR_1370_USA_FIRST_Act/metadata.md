# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1370
- Title: USA FIRST Act
- Congress: 119
- Bill type: HR
- Bill number: 1370
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-06-24T13:28:23Z
- Update date including text: 2025-06-24T13:28:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1370",
    "number": "1370",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001317",
        "district": "2",
        "firstName": "Josh",
        "fullName": "Rep. Brecheen, Josh [R-OK-2]",
        "lastName": "Brecheen",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "USA FIRST Act",
    "type": "HR",
    "updateDate": "2025-06-24T13:28:23Z",
    "updateDateIncludingText": "2025-06-24T13:28:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:33:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "SC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1370ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1370\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Brecheen (for himself, Mr. Norman , and Mr. Donalds ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo transfer unobligated funds from the United States Agency for International Development to the Disaster Relief Fund.\n#### 1. Short title\nThis Act may be cited as the Unobligated Spending Adjustment to Focus Investment on Relief and Support for Taxpayers Act or the USA FIRST Act .\n#### 2. Transfer of unobligated funds to the disaster relief fund\n##### (a) In general\nAny unobligated covered funds shall be transferred to the Disaster Relief Fund to carry out the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) with respect to major disasters declared under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ).\n##### (b) Covered funds defined\nIn this section, the term \u201ccovered funds\u201d means any unobligated funds previously appropriated to the United States Agency for International Development, as of the date of enactment of this Act.",
      "versionDate": "2025-02-14",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-14T13:13:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1370",
          "measure-number": "1370",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1370v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Unobligated Spending Adjustment to Focus Investment on Relief and Support for Taxpayers Act or the USA FIRST Act</strong></p><p>This bill transfers unobligated funds previously appropriated to the U.S. Agency for International Development to the Disaster Relief Fund (DRF) for general disaster relief for major disasters declared by the President. The\u00a0DRF is managed by the Federal Emergency Management Agency and the activities it funds pursuant to major disaster declarations include domestic disaster response, recovery, and mitigation.</p>"
        },
        "title": "USA FIRST Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1370.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Unobligated Spending Adjustment to Focus Investment on Relief and Support for Taxpayers Act or the USA FIRST Act</strong></p><p>This bill transfers unobligated funds previously appropriated to the U.S. Agency for International Development to the Disaster Relief Fund (DRF) for general disaster relief for major disasters declared by the President. The\u00a0DRF is managed by the Federal Emergency Management Agency and the activities it funds pursuant to major disaster declarations include domestic disaster response, recovery, and mitigation.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119hr1370"
    },
    "title": "USA FIRST Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Unobligated Spending Adjustment to Focus Investment on Relief and Support for Taxpayers Act or the USA FIRST Act</strong></p><p>This bill transfers unobligated funds previously appropriated to the U.S. Agency for International Development to the Disaster Relief Fund (DRF) for general disaster relief for major disasters declared by the President. The\u00a0DRF is managed by the Federal Emergency Management Agency and the activities it funds pursuant to major disaster declarations include domestic disaster response, recovery, and mitigation.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119hr1370"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1370ih.xml"
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
      "title": "USA FIRST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USA FIRST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unobligated Spending Adjustment to Focus Investment on Relief and Support for Taxpayers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To transfer unobligated funds from the United States Agency for International Development to the Disaster Relief Fund.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T04:18:30Z"
    }
  ]
}
```
