# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2810?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2810
- Title: Retirement Freedom Act
- Congress: 119
- Bill type: S
- Bill number: 2810
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-12-05T21:38:46Z
- Update date including text: 2025-12-05T21:38:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2810",
    "number": "2810",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Retirement Freedom Act",
    "type": "S",
    "updateDate": "2025-12-05T21:38:46Z",
    "updateDateIncludingText": "2025-12-05T21:38:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T15:16:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2810is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2810\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Mr. Cruz (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo allow individuals to choose to opt out of the Medicare part A benefit.\n#### 1. Short title\nThis Act may be cited as the Retirement Freedom Act .\n#### 2. Allowing individuals to choose to opt out of the Medicare part A benefit\nAny individual who is otherwise entitled to benefits under part A of title XVIII of the Social Security Act may elect (in such form and manner as may be specified by the Secretary of Health and Human Services) to opt out of such entitlement. Notwithstanding any other provision of law, in the case of an individual who makes such an election, such individual\u2014\n**(1)**\nmay (in such form and manner as may be specified by the Secretary) subsequently choose to end such election and opt back into such entitlement (in accordance with a process determined by the Secretary) without being subject to any penalty;\n**(2)**\nshall not be required to opt out of benefits under title II of such Act as a condition for making such election; and\n**(3)**\nshall not be required to repay any amount paid under such part A for items and services furnished prior to making such election.",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2793",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Retirement Freedom Act",
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
        "name": "Health",
        "updateDate": "2025-09-29T19:28:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-16",
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
          "measure-id": "id119s2810",
          "measure-number": "2810",
          "measure-type": "s",
          "orig-publish-date": "2025-09-16",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2810v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-09-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Retirement Freedom Act</strong></p><p>This bill allows an individual to opt out of Medicare hospital services benefits without also having to opt out of Social Security benefits and without having to repay Medicare hospital services benefits already received. The bill also allows an individual to opt back in with no penalty.</p>"
        },
        "title": "Retirement Freedom Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2810.xml",
    "summary": {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Retirement Freedom Act</strong></p><p>This bill allows an individual to opt out of Medicare hospital services benefits without also having to opt out of Social Security benefits and without having to repay Medicare hospital services benefits already received. The bill also allows an individual to opt back in with no penalty.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2810"
    },
    "title": "Retirement Freedom Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Retirement Freedom Act</strong></p><p>This bill allows an individual to opt out of Medicare hospital services benefits without also having to opt out of Social Security benefits and without having to repay Medicare hospital services benefits already received. The bill also allows an individual to opt back in with no penalty.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2810"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2810is.xml"
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
      "title": "Retirement Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retirement Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow individuals to choose to opt out of the Medicare part A benefit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:24Z"
    }
  ]
}
```
