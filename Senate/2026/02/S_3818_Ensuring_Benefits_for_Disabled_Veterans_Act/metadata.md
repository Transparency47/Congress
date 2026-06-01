# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3818?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3818
- Title: Ensuring Benefits for Disabled Veterans Act
- Congress: 119
- Bill type: S
- Bill number: 3818
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-03-02T16:04:39Z
- Update date including text: 2026-03-02T16:04:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3818",
    "number": "3818",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Ensuring Benefits for Disabled Veterans Act",
    "type": "S",
    "updateDate": "2026-03-02T16:04:39Z",
    "updateDateIncludingText": "2026-03-02T16:04:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T20:07:13Z",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3818is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3818\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. King (for himself and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Veteran Readiness and Employment program and the educational assistance programs of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Ensuring Benefits for Disabled Veterans Act .\n#### 2. Repeal of certain limitation on receipt of assistance under both the Veteran Readiness and Employment program and the educational assistance programs of the Department of Veterans Affairs\nSection 3695 of title 38, United States Code, is amended\u2014\n**(1)**\nby striking subsection (b); and\n**(2)**\nby redesignating subsection (c) as subsection (b).",
      "versionDate": "2026-02-10",
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
        "actionDate": "2026-02-10",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "7472",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Department of Veterans Affairs Veteran Readiness and Employment program and Department of Veterans Affairs educational assistance programs.",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-27T21:42:01Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3818is.xml"
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
      "title": "Ensuring Benefits for Disabled Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T05:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Benefits for Disabled Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to repeal a certain limitation on the receipt of assistance under both the Veteran Readiness and Employment program and the educational assistance programs of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:33:28Z"
    }
  ]
}
```
