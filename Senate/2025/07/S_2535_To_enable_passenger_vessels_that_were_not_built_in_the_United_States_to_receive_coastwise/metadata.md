# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2535?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2535
- Title: Protecting Jobs in American Ports Act
- Congress: 119
- Bill type: S
- Bill number: 2535
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2025-09-17T16:16:40Z
- Update date including text: 2025-09-17T16:16:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2535",
    "number": "2535",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Protecting Jobs in American Ports Act",
    "type": "S",
    "updateDate": "2025-09-17T16:16:40Z",
    "updateDateIncludingText": "2025-09-17T16:16:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T17:32:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2535is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2535\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo enable passenger vessels that were not built in the United States to receive coastwise endorsement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Jobs in American Ports Act .\n#### 2. Coastwise endorsement for passenger vessels\n##### (a) In general\nSection 12112(a)(2)(B) of title 46, United States Code, is amended\u2014\n**(1)**\nin clause (ii), by striking ; or and inserting a semicolon;\n**(2)**\nin clause (iii), by striking ; and and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(iv) is a vessel that transports passengers between ports or places in the United States to which the coastwise laws apply, either directly or via a foreign port; and .\n##### (b) Conforming amendment\nSection 12121 of title 46, United States Code, is repealed.\n##### (c) Rule of construction\nNothing in the amendments made by this section shall be construed to exempt a vessel that transports passengers between ports or places in the United States to which the coastwise laws apply, either directly or via a foreign port, from any applicable law of the United States except as explicitly provided in such amendments.",
      "versionDate": "2025-07-30",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-17T16:16:40Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2535is.xml"
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
      "title": "Protecting Jobs in American Ports Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Jobs in American Ports Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enable passenger vessels that were not built in the United States to receive coastwise endorsement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T04:48:17Z"
    }
  ]
}
```
