# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/8?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/8
- Title: Reaffirming the House of Representatives's commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections.
- Congress: 119
- Bill type: HRES
- Bill number: 8
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-16T21:48:58Z
- Update date including text: 2025-01-16T21:48:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/8",
    "number": "8",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Reaffirming the House of Representatives's commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections.",
    "type": "HRES",
    "updateDate": "2025-01-16T21:48:58Z",
    "updateDateIncludingText": "2025-01-16T21:48:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-03T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres8ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 8\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Crane ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nReaffirming the House of Representatives\u2019s commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections.\nThat the House of Representatives\u2014\n**(1)**\nreaffirms and reiterates its commitment to ensuring secure elections throughout the United States; and\n**(2)**\nrecognizes that the presentation of valid photograph identification is a fundamental component of secure elections throughout the United States.",
      "versionDate": "2025-01-03",
      "versionType": "IH"
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
        "item": {
          "name": "Elections, voting, political campaign regulation",
          "updateDate": "2025-01-15T18:36:22Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-01-14T16:15:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hres8",
          "measure-number": "8",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres8v00",
            "update-date": "2025-01-16"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses that the House of Representatives (1) reaffirms and reiterates its commitment to ensuring secure elections throughout the United States, and (2) recognizes that the presentation of valid photograph identification is a fundamental component of secure elections throughout the United States.</p>"
        },
        "title": "Reaffirming the House of Representatives's commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres8.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses that the House of Representatives (1) reaffirms and reiterates its commitment to ensuring secure elections throughout the United States, and (2) recognizes that the presentation of valid photograph identification is a fundamental component of secure elections throughout the United States.</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hres8"
    },
    "title": "Reaffirming the House of Representatives's commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses that the House of Representatives (1) reaffirms and reiterates its commitment to ensuring secure elections throughout the United States, and (2) recognizes that the presentation of valid photograph identification is a fundamental component of secure elections throughout the United States.</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hres8"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres8ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Reaffirming the House of Representatives's commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reaffirming the House of Representatives's commitment to ensuring secure elections throughout the United States by recognizing that the presentation of valid photograph identification is a fundamental component of secure elections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:19Z"
    }
  ]
}
```
