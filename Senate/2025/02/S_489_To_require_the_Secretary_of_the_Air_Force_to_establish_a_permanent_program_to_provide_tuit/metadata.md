# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/489
- Title: Air Guard STATUS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 489
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-08T15:41:57Z
- Update date including text: 2025-12-08T15:41:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/489",
    "number": "489",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Air Guard STATUS Act of 2025",
    "type": "S",
    "updateDate": "2025-12-08T15:41:57Z",
    "updateDateIncludingText": "2025-12-08T15:41:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-07T00:44:56Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s489is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 489\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Hoeven (for himself, Mrs. Shaheen , Mr. Moran , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of the Air Force to establish a permanent program to provide tuition assistance to members of the Air National Guard.\n#### 1. Short title\nThis Act may be cited as the Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025 .\n#### 2. Provision of tuition assistance to members of Air National Guard\nThe Secretary of the Air Force shall establish a permanent program to pay, under section 2007 of title 10, United States Code, all or a portion of the charges of an educational institution for the tuition or expenses of a member of the Air National Guard who is in compliance with the training requirements under regulations prescribed under section 502(a) of title 32, United States Code.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-12-04",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "6478",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Air Guard STATUS Act of 2025",
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
            "name": "Aviation and airports",
            "updateDate": "2025-06-13T18:47:54Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-06-13T18:48:09Z"
          },
          {
            "name": "Military education and training",
            "updateDate": "2025-06-13T18:47:59Z"
          },
          {
            "name": "National Guard and reserves",
            "updateDate": "2025-06-13T18:48:15Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-06-13T18:48:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-05T13:36:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s489",
          "measure-number": "489",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s489v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025</strong></p><p>This bill requires the Department of the Air Force to establish a permanent program to pay all or a portion of tuition or expenses at an educational institution for members of the Air National Guard who are in compliance with training requirements (i.e., required field exercises and drills).</p>"
        },
        "title": "Air Guard STATUS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s489.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025</strong></p><p>This bill requires the Department of the Air Force to establish a permanent program to pay all or a portion of tuition or expenses at an educational institution for members of the Air National Guard who are in compliance with training requirements (i.e., required field exercises and drills).</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s489"
    },
    "title": "Air Guard STATUS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025</strong></p><p>This bill requires the Department of the Air Force to establish a permanent program to pay all or a portion of tuition or expenses at an educational institution for members of the Air National Guard who are in compliance with training requirements (i.e., required field exercises and drills).</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s489"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s489is.xml"
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
      "title": "Air Guard STATUS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Air Guard STATUS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Air Force to establish a permanent program to provide tuition assistance to members of the Air National Guard.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:35:01Z"
    }
  ]
}
```
