# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/30?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/30
- Title: A resolution honoring Mississippi's Gestational Age Act.
- Congress: 119
- Bill type: SRES
- Bill number: 30
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S302-303)
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S302-303)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/30",
    "number": "30",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "A resolution honoring Mississippi's Gestational Age Act.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S302-303)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T20:20:11Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MS"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ND"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "KS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "NE"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "UT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres30is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 30\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mrs. Hyde-Smith (for herself, Mr. Wicker , Mr. Hoeven , Mr. Marshall , Mr. Ricketts , Mr. Lee , and Mr. Banks ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring Mississippi's Gestational Age Act.\nThat the Senate\u2014\n**(1)**\nexpresses profound gratitude to Mississippi State Representative Becky Currie for introducing the catalyst that ultimately brought about the historical victory of overturning Roe v. Wade, 410 U.S. 113 (1973) and Planned Parenthood v. Casey, 503 U.S. 833 (1992); and\n**(2)**\nhonors life-affirming States across the country that have enacted laws aimed to value and protect the inherent dignity of every mother and unborn child.",
      "versionDate": "2025-01-22",
      "versionType": "IS"
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
            "name": "Abortion",
            "updateDate": "2025-02-03T17:15:16Z"
          },
          {
            "name": "Mississippi",
            "updateDate": "2025-02-03T17:15:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-01-27T13:51:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119sres30",
          "measure-number": "30",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres30v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses gratitude to Mississippi State Representative Becky Currie for introducing the state legislation prohibiting abortion after 15 weeks that resulted in the U.S. Supreme Court\u2019s <em>Dobbs v. Jackson Women\u2019s Health Organization</em> decision overturning <em>Roe v. Wade</em> and <em>Planned Parenthood of Southeastern Pennsylvania v. Casey</em>.</p>"
        },
        "title": "A resolution honoring Mississippi's Gestational Age Act."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres30.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses gratitude to Mississippi State Representative Becky Currie for introducing the state legislation prohibiting abortion after 15 weeks that resulted in the U.S. Supreme Court\u2019s <em>Dobbs v. Jackson Women\u2019s Health Organization</em> decision overturning <em>Roe v. Wade</em> and <em>Planned Parenthood of Southeastern Pennsylvania v. Casey</em>.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119sres30"
    },
    "title": "A resolution honoring Mississippi's Gestational Age Act."
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses gratitude to Mississippi State Representative Becky Currie for introducing the state legislation prohibiting abortion after 15 weeks that resulted in the U.S. Supreme Court\u2019s <em>Dobbs v. Jackson Women\u2019s Health Organization</em> decision overturning <em>Roe v. Wade</em> and <em>Planned Parenthood of Southeastern Pennsylvania v. Casey</em>.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119sres30"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres30is.xml"
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
      "title": "A resolution honoring Mississippi's Gestational Age Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-25T05:03:40Z"
    },
    {
      "title": "A resolution honoring Mississippi's Gestational Age Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T11:56:15Z"
    }
  ]
}
```
