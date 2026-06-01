# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/430
- Title: A resolution designating October 4, 2025, as "National Energy Appreciation Day" to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world.
- Congress: 119
- Bill type: SRES
- Bill number: 430
- Origin chamber: Senate
- Introduced date: 2025-10-03
- Update date: 2026-04-09T10:43:36Z
- Update date including text: 2026-04-09T10:43:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in Senate
- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6934-6935)
- Latest action: 2025-10-03: Introduced in Senate

## Actions

- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6934-6935)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/430",
    "number": "430",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A resolution designating October 4, 2025, as \"National Energy Appreciation Day\" to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world.",
    "type": "SRES",
    "updateDate": "2026-04-09T10:43:36Z",
    "updateDateIncludingText": "2026-04-09T10:43:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S6934-6935)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T16:18:44Z",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "SC"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "OK"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "ID"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "WV"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "ID"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "WV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "MS"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "ND"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "WY"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "ND"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "OH"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres430is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 430\nIN THE SENATE OF THE UNITED STATES\nOctober 3, 2025 Ms. Lummis (for herself, Mr. Scott of South Carolina , Mr. Lankford , Mr. Crapo , Mrs. Capito , Mr. Risch , Mr. Justice , Mrs. Hyde-Smith , Mr. Hoeven , Mr. Cassidy , Mr. Cruz , Mr. Barrasso , Mr. Cramer , and Mr. Husted ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating October 4, 2025, as National Energy Appreciation Day to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world.\nThat the Senate\u2014\n**(1)**\ndesignates October 4, 2025, as National Energy Appreciation Day ; and\n**(2)**\nencourages the Federal Government, States, localities, schools, nonprofit organizations, businesses, and the people of the United States to observe National Energy Appreciation Day with appropriate events to promote education on, and celebrate the role of, modern energy systems in everyday life.",
      "versionDate": "2025-10-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-12-05T15:34:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119sres430",
          "measure-number": "430",
          "measure-type": "sres",
          "orig-publish-date": "2025-10-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres430v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates October 4, 2025, as National Energy Appreciation Day.</p>"
        },
        "title": "A resolution designating October 4, 2025, as \"National Energy Appreciation Day\" to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres430.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates October 4, 2025, as National Energy Appreciation Day.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119sres430"
    },
    "title": "A resolution designating October 4, 2025, as \"National Energy Appreciation Day\" to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world."
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates October 4, 2025, as National Energy Appreciation Day.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119sres430"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres430is.xml"
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
      "title": "A resolution designating October 4, 2025, as \"National Energy Appreciation Day\" to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-09T04:33:14Z"
    },
    {
      "title": "A resolution designating October 4, 2025, as \"National Energy Appreciation Day\" to celebrate the people who work to power the United States and the economy of the United States and to build awareness of the important role that the energy producers of the United States play in reducing poverty, strengthening national security, and improving the quality of life for people around the world.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:56:14Z"
    }
  ]
}
```
