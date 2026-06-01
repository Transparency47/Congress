# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1539
- Title: Depot Investment Reform Act
- Congress: 119
- Bill type: S
- Bill number: 1539
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-12-06T07:02:23Z
- Update date including text: 2025-12-06T07:02:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1539",
    "number": "1539",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Depot Investment Reform Act",
    "type": "S",
    "updateDate": "2025-12-06T07:02:23Z",
    "updateDateIncludingText": "2025-12-06T07:02:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T19:57:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1539is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1539\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Fetterman (for himself and Mr. Cotton ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to modify the minimum capital investment for certain depots of the Department of Defense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Depot Investment Reform Act .\n#### 2. Modification of minimum capital investment for certain depots of Department of Defense\nSection 2476(a)(1) of title 10, United States Code, is amended by striking the preceding three fiscal years and inserting the preceding fiscal year, the current fiscal year, and the estimated amount for the following fiscal year .",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "3336",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Depot Investment Reform Act of 2025",
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
        "updateDate": "2025-05-23T00:06:13Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1539is.xml"
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
      "title": "Depot Investment Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Depot Investment Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to modify the minimum capital investment for certain depots of the Department of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:22Z"
    }
  ]
}
```
