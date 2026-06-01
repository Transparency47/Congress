# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1267?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1267
- Title: Deliver for Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1267
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-07-01T20:55:12Z
- Update date including text: 2025-07-01T20:55:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1267",
    "number": "1267",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Deliver for Veterans Act of 2025",
    "type": "S",
    "updateDate": "2025-07-01T20:55:12Z",
    "updateDateIncludingText": "2025-07-01T20:55:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:08:49Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1267is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1267\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Ms. Murkowski (for herself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to pay costs associated with the delivery of automobiles adapted for operation by a disabled individual to eligible persons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deliver for Veterans Act of 2025 .\n#### 2. Authority of the Secretary of Veterans Affairs to pay costs associated with delivery of automobiles or other conveyances to eligible persons\nSection 3902(a) of title 38, United States Code, is amended by inserting and the total shipping price to deliver the automobile or other conveyance to the eligible person after the total purchase price of the automobile or other conveyance .",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T18:15:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
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
          "measure-id": "id119s1267",
          "measure-number": "1267",
          "measure-type": "s",
          "orig-publish-date": "2025-04-02",
          "originChamber": "SENATE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1267v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Deliver for Veterans Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to include delivery costs when paying the full purchase price of an automobile or other conveyance for certain disabled veterans or members of the Armed Forces. Currently, the VA must pay the lesser of (1) $26,417.20 (adjusted annually for inflation), or (2) the full purchase price associated with providing an automobile or other conveyance to such individuals (not including delivery costs).</p>"
        },
        "title": "Deliver for Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1267.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Deliver for Veterans Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to include delivery costs when paying the full purchase price of an automobile or other conveyance for certain disabled veterans or members of the Armed Forces. Currently, the VA must pay the lesser of (1) $26,417.20 (adjusted annually for inflation), or (2) the full purchase price associated with providing an automobile or other conveyance to such individuals (not including delivery costs).</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119s1267"
    },
    "title": "Deliver for Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Deliver for Veterans Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to include delivery costs when paying the full purchase price of an automobile or other conveyance for certain disabled veterans or members of the Armed Forces. Currently, the VA must pay the lesser of (1) $26,417.20 (adjusted annually for inflation), or (2) the full purchase price associated with providing an automobile or other conveyance to such individuals (not including delivery costs).</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119s1267"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1267is.xml"
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
      "title": "Deliver for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deliver for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to pay costs associated with the delivery of automobiles adapted for operation by a disabled individual to eligible persons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:39Z"
    }
  ]
}
```
