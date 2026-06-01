# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/78?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/78
- Title: A joint resolution proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns.
- Congress: 119
- Bill type: SJRES
- Bill number: 78
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-04-08T20:03:03Z
- Update date including text: 2026-04-08T20:03:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/78",
    "number": "78",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A joint resolution proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns.",
    "type": "SJRES",
    "updateDate": "2026-04-08T20:03:03Z",
    "updateDateIncludingText": "2026-04-08T20:03:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
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
            "date": "2025-09-17T15:34:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-17T15:34:58Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NH"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-09-17",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NJ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NJ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "AZ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres78is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 78\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Schiff (for himself, Mrs. Shaheen , Mr. King , Mr. Welch , Mr. Whitehouse , Mr. Kim , and Mr. Booker ) introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. Congress and the States may regulate and impose reasonable viewpoint-neutral limitations on the raising and spending of money by candidates and others to influence elections. 2. Congress and the States may regulate and enact systems of public campaign financing, including those designed to restrict the influence of private wealth by offsetting the raising and spending of money by candidates and others to influence elections with increased public funding. 3. Congress and the States shall have power to implement and enforce this article by appropriate legislation, and may distinguish between natural persons and corporations or other artificial entities created by law, including by prohibiting such entities from spending money to influence elections. 4. Nothing in this article shall be construed to grant Congress or the States the power to abridge the freedom of the press. .",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-09-17",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "122",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns.",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-23T18:22:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-17",
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
          "measure-id": "id119sjres78",
          "measure-number": "78",
          "measure-type": "sjres",
          "orig-publish-date": "2025-09-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres78v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-09-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong></strong>This joint resolution proposes a constitutional amendment authorizing Congress and the states to (1) regulate and impose reasonable viewpoint-neutral limitations on the raising and spending of money by candidates and others to influence elections; and (2) regulate and enact public campaign financing systems, including those designed to restrict the influence of private wealth by offsetting the raising and spending of money by candidates and others with increased public funding. </p> <p>The amendment grants Congress and the states the power to implement and enforce this amendment by legislation. They are allowed to distinguish between natural persons and corporations or other artificial entities created by law, including by prohibiting such entities from spending money to influence elections.</p>"
        },
        "title": "A joint resolution proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres78.xml",
    "summary": {
      "actionDate": "2025-09-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong></strong>This joint resolution proposes a constitutional amendment authorizing Congress and the states to (1) regulate and impose reasonable viewpoint-neutral limitations on the raising and spending of money by candidates and others to influence elections; and (2) regulate and enact public campaign financing systems, including those designed to restrict the influence of private wealth by offsetting the raising and spending of money by candidates and others with increased public funding. </p> <p>The amendment grants Congress and the states the power to implement and enforce this amendment by legislation. They are allowed to distinguish between natural persons and corporations or other artificial entities created by law, including by prohibiting such entities from spending money to influence elections.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sjres78"
    },
    "title": "A joint resolution proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns."
  },
  "summaries": [
    {
      "actionDate": "2025-09-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong></strong>This joint resolution proposes a constitutional amendment authorizing Congress and the states to (1) regulate and impose reasonable viewpoint-neutral limitations on the raising and spending of money by candidates and others to influence elections; and (2) regulate and enact public campaign financing systems, including those designed to restrict the influence of private wealth by offsetting the raising and spending of money by candidates and others with increased public funding. </p> <p>The amendment grants Congress and the states the power to implement and enforce this amendment by legislation. They are allowed to distinguish between natural persons and corporations or other artificial entities created by law, including by prohibiting such entities from spending money to influence elections.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sjres78"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres78is.xml"
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
      "title": "A joint resolution proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:17Z"
    },
    {
      "title": "A joint resolution proposing an amendment to the Constitution of the United States relating to the authority of Congress and the States to regulate contributions and expenditures intended to affect elections and to enact public financing systems for political campaigns.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T10:56:19Z"
    }
  ]
}
```
