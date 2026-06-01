# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/1?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/1
- Title: Proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices.
- Congress: 119
- Bill type: HJRES
- Bill number: 1
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-07-17T11:33:12Z
- Update date including text: 2025-07-17T11:33:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/1",
    "number": "1",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
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
    "title": "Proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices.",
    "type": "HJRES",
    "updateDate": "2025-07-17T11:33:12Z",
    "updateDateIncludingText": "2025-07-17T11:33:12Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres1ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 1\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 The Supreme Court of the United States shall be composed of nine justices consisting of one chief justice and eight associate justices. .",
      "versionDate": "2025-01-03",
      "versionType": "IH"
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
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "16",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices.",
      "type": "SJRES"
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
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:32:59Z"
          },
          {
            "name": "Judges",
            "updateDate": "2025-01-15T18:32:59Z"
          },
          {
            "name": "Supreme Court",
            "updateDate": "2025-01-15T18:32:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-01-07T12:25:02Z"
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
          "measure-id": "id119hjres1",
          "measure-number": "1",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres1v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment requiring the Supreme Court to be composed\u00a0of nine Justices\u2014one Chief Justice and eight Associate Justices.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres1.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment requiring the Supreme Court to be composed\u00a0of nine Justices\u2014one Chief Justice and eight Associate Justices.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres1"
    },
    "title": "Proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment requiring the Supreme Court to be composed\u00a0of nine Justices\u2014one Chief Justice and eight Associate Justices.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres1"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres1ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to require that the Supreme Court of the United States be composed of nine justices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:19Z"
    }
  ]
}
```
