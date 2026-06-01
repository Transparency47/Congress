# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3138?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3138
- Title: Veterans SPORT Act
- Congress: 119
- Bill type: S
- Bill number: 3138
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3138",
    "number": "3138",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Veterans SPORT Act",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
            "date": "2026-03-18T20:00:32Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-06T19:54:28Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-06T19:54:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-11-06",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "AL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3138is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3138\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Banks (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to include adaptive prostheses and terminal devices for sports and other recreational activities in the medical services furnished to eligible veterans by the Secretary of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act .\n#### 2. Inclusion of adaptive prostheses and terminal devices for sports and other recreational activities in medical services furnished to eligible veterans by the Secretary of Veterans Affairs\nSection 1701 of title 38, United States Code, is amended, in paragraph (6)(F)(i), by inserting (including adaptive prostheses and terminal devices for sports and other recreational activities) after artificial limbs .",
      "versionDate": "2025-11-06",
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
        "actionDate": "2025-03-25",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "1971",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans SPORT Act",
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
            "name": "Athletes",
            "updateDate": "2026-04-16T19:19:17Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2026-04-16T19:19:17Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2026-04-16T19:19:17Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-04-16T19:19:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:43:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-06",
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
          "measure-id": "id119s3138",
          "measure-number": "3138",
          "measure-type": "s",
          "orig-publish-date": "2025-11-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3138v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-11-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act</strong></p><p>This bill includes adaptive prostheses and terminal devices for sports and other recreational activities within the definition of <em>medical services</em> under the laws administered by the Department of Veterans Affairs (VA). Under the bill, these artificial limbs must be furnished as medical services to eligible veterans.</p>"
        },
        "title": "Veterans SPORT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3138.xml",
    "summary": {
      "actionDate": "2025-11-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act</strong></p><p>This bill includes adaptive prostheses and terminal devices for sports and other recreational activities within the definition of <em>medical services</em> under the laws administered by the Department of Veterans Affairs (VA). Under the bill, these artificial limbs must be furnished as medical services to eligible veterans.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3138"
    },
    "title": "Veterans SPORT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act</strong></p><p>This bill includes adaptive prostheses and terminal devices for sports and other recreational activities within the definition of <em>medical services</em> under the laws administered by the Department of Veterans Affairs (VA). Under the bill, these artificial limbs must be furnished as medical services to eligible veterans.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3138"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3138is.xml"
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
      "title": "Veterans SPORT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans SPORT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to include adaptive prostheses and terminal devices for sports and other recreational activities in the medical services furnished to eligible veterans by the Secretary of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:18:31Z"
    }
  ]
}
```
