# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/5?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/5
- Title: Proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress.
- Congress: 119
- Bill type: HJRES
- Bill number: 5
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-05T21:27:16Z
- Update date including text: 2025-12-05T21:27:16Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/5",
    "number": "5",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress.",
    "type": "HJRES",
    "updateDate": "2025-12-05T21:27:16Z",
    "updateDateIncludingText": "2025-12-05T21:27:16Z"
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
          "date": "2025-01-03T16:25:45Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres5ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 5\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick (for himself and Mr. Khanna ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. No person shall serve as a Representative for more than six two-year terms. Service as a Representative for more than one year of any two-year term shall be treated as a complete term for purposes of this section, without regard to whether the service was completed by the individual originally elected to the term. 2. No person shall serve as a Senator for more than two six-year terms. Service as a Senator for more than three years of any six-year term shall be treated as a complete term for purposes of this section, without regard to whether the service was completed by the individual originally elected to the term. 3. This article shall not apply to any person who served as a Representative or as a Senator during any Congress occurring before the One Hundred Eighteenth Congress. .",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "48",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress.",
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
            "name": "Congressional elections",
            "updateDate": "2025-01-15T18:54:44Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:54:44Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:54:44Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-15T18:54:44Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-15T18:54:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-07T12:16:03Z"
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
          "measure-id": "id119hjres5",
          "measure-number": "5",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres5v00",
            "update-date": "2025-01-16"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes an amendment to the\u00a0Constitution to limit terms in the Senate and the House of Representatives.</p><p>Specifically, the amendment limits an individual serving as a Member of the House of Representatives to six two-year terms and an individual serving as a Senator to two six-year terms. The amendment specifies that the term limits do not apply to an individual who served in either chamber of Congress before the 118th Congress.\u00a0</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.\u00a0</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres5.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes an amendment to the\u00a0Constitution to limit terms in the Senate and the House of Representatives.</p><p>Specifically, the amendment limits an individual serving as a Member of the House of Representatives to six two-year terms and an individual serving as a Senator to two six-year terms. The amendment specifies that the term limits do not apply to an individual who served in either chamber of Congress before the 118th Congress.\u00a0</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.\u00a0</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hjres5"
    },
    "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes an amendment to the\u00a0Constitution to limit terms in the Senate and the House of Representatives.</p><p>Specifically, the amendment limits an individual serving as a Member of the House of Representatives to six two-year terms and an individual serving as a Senator to two six-year terms. The amendment specifies that the term limits do not apply to an individual who served in either chamber of Congress before the 118th Congress.\u00a0</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.\u00a0</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hjres5"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres5ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms an individual may serve as a Member of Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:33Z"
    }
  ]
}
```
