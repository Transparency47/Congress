# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/38?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/38
- Title: A joint resolution establishing the ratification of the Equal Rights Amendment.
- Congress: 119
- Bill type: SJRES
- Bill number: 38
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-04-06T18:32:29Z
- Update date including text: 2026-04-06T18:32:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/38",
    "number": "38",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A joint resolution establishing the ratification of the Equal Rights Amendment.",
    "type": "SJRES",
    "updateDate": "2026-04-06T18:32:29Z",
    "updateDateIncludingText": "2026-04-06T18:32:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T21:01:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "HI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "ME"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres38is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 38\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Ms. Murkowski (for herself and Ms. Hirono ) introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nEstablishing the ratification of the Equal Rights Amendment.\nThat notwithstanding any time limit contained in House Joint Resolution 208, 92nd Congress, as agreed to in the Senate on March 22, 1972, the article of amendment proposed to the States in that joint resolution is valid to all intents and purposes as part of the Constitution, having been ratified by the legislatures of three-fourths of the several States.",
      "versionDate": "2025-03-25",
      "versionType": "IS"
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
        "actionDate": "2025-03-24",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "80",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Establishing the ratification of the Equal Rights Amendment.",
      "type": "HJRES"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-31T13:23:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119sjres38",
          "measure-number": "38",
          "measure-type": "sjres",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres38v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution provides that the Equal Rights Amendment, which prohibits discrimination on the basis of sex, was ratified by three-fourths of the states and is therefore a valid constitutional amendment, regardless of any time limit that was in the original proposal. </p> <p>The Equal Rights Amendment was originally proposed to the states in 1972. The original proposal included a deadline for ratification of March 22, 1979; Congress subsequently extended the deadline to June 30, 1982. Although the requisite 38 states have ratified the amendment, three of these states did so after the deadlines, and five states subsequently rescinded their ratifications. The status of the amendment has been the subject of litigation.</p>"
        },
        "title": "A joint resolution establishing the ratification of the Equal Rights Amendment."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres38.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution provides that the Equal Rights Amendment, which prohibits discrimination on the basis of sex, was ratified by three-fourths of the states and is therefore a valid constitutional amendment, regardless of any time limit that was in the original proposal. </p> <p>The Equal Rights Amendment was originally proposed to the states in 1972. The original proposal included a deadline for ratification of March 22, 1979; Congress subsequently extended the deadline to June 30, 1982. Although the requisite 38 states have ratified the amendment, three of these states did so after the deadlines, and five states subsequently rescinded their ratifications. The status of the amendment has been the subject of litigation.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sjres38"
    },
    "title": "A joint resolution establishing the ratification of the Equal Rights Amendment."
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution provides that the Equal Rights Amendment, which prohibits discrimination on the basis of sex, was ratified by three-fourths of the states and is therefore a valid constitutional amendment, regardless of any time limit that was in the original proposal. </p> <p>The Equal Rights Amendment was originally proposed to the states in 1972. The original proposal included a deadline for ratification of March 22, 1979; Congress subsequently extended the deadline to June 30, 1982. Although the requisite 38 states have ratified the amendment, three of these states did so after the deadlines, and five states subsequently rescinded their ratifications. The status of the amendment has been the subject of litigation.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sjres38"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres38is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution establishing the ratification of the Equal Rights Amendment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T10:48:22Z"
    },
    {
      "title": "A joint resolution establishing the ratification of the Equal Rights Amendment.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T10:56:19Z"
    }
  ]
}
```
