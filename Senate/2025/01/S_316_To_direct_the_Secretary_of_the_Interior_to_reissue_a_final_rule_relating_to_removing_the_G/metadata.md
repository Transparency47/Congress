# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/316
- Title: Grizzly Bear State Management Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 316
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-02-25T12:50:28Z
- Update date including text: 2026-02-25T12:50:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/316",
    "number": "316",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
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
    "title": "Grizzly Bear State Management Act of 2025",
    "type": "S",
    "updateDate": "2026-02-25T12:50:28Z",
    "updateDateIncludingText": "2026-02-25T12:50:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T21:34:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s316is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 316\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Lummis (for herself, Mr. Barrasso , Mr. Sheehy , Mr. Daines , Mr. Risch , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo direct the Secretary of the Interior to reissue a final rule relating to removing the Greater Yellowstone Ecosystem population of grizzly bears from the Federal list of endangered and threatened wildlife, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Grizzly Bear State Management Act of 2025 .\n#### 2. Reissuance of final rule relating to Greater Yellowstone Ecosystem population of grizzly bears\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of the Interior shall reissue the final rule entitled Endangered and Threatened Wildlife and Plants; Removing the Greater Yellowstone Ecosystem Population of Grizzly Bears From the Federal List of Endangered and Threatened Wildlife (82 Fed. Reg. 30502 (June 30, 2017)), without regard to any other provision of law that applies to the issuance of that final rule.\n##### (b) No judicial review\nThe reissuance of the final rule described in subsection (a) (including this section) shall not be subject to judicial review.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-10-03",
        "text": "Placed on the Union Calendar, Calendar No. 281."
      },
      "number": "281",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Grizzly Bear State Management Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-03-06T17:00:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s316",
          "measure-number": "316",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s316v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Grizzly Bear State Management Act of 2025</strong></p><p>This bill requires the Department of the Interior to remove the Greater Yellowstone ecosystem population of grizzly bears from the list of endangered and threatened wildlife.</p>"
        },
        "title": "Grizzly Bear State Management Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s316.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Grizzly Bear State Management Act of 2025</strong></p><p>This bill requires the Department of the Interior to remove the Greater Yellowstone ecosystem population of grizzly bears from the list of endangered and threatened wildlife.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s316"
    },
    "title": "Grizzly Bear State Management Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Grizzly Bear State Management Act of 2025</strong></p><p>This bill requires the Department of the Interior to remove the Greater Yellowstone ecosystem population of grizzly bears from the list of endangered and threatened wildlife.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s316"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s316is.xml"
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
      "title": "Grizzly Bear State Management Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Grizzly Bear State Management Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior to reissue a final rule relating to removing the Greater Yellowstone Ecosystem population of grizzly bears from the Federal list of endangered and threatened wildlife, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:30Z"
    }
  ]
}
```
