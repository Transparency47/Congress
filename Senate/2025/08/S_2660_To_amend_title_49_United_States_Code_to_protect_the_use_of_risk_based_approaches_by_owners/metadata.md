# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2660
- Title: Modern Risk Detection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2660
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-18T20:12:30Z
- Update date including text: 2025-09-18T20:12:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2660",
    "number": "2660",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Modern Risk Detection Act of 2025",
    "type": "S",
    "updateDate": "2025-09-18T20:12:30Z",
    "updateDateIncludingText": "2025-09-18T20:12:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T21:27:22Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2660is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2660\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Curtis introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to protect the use of risk-based approaches by owners and operators of certain pipeline facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modern Risk Detection Act of 2025 .\n#### 2. Risk-based approaches\nSection 60102 of title 49, United States Code, is amended by adding at the end the following:\n(u) Risk-Based approaches The Secretary shall ensure that the standards prescribed under this chapter allow for the use, to the maximum extent practicable, of risk-based approaches, concepts, or principles in complying with those standards. .",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-18T20:12:30Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2660is.xml"
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
      "title": "Modern Risk Detection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Modern Risk Detection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to protect the use of risk-based approaches by owners and operators of certain pipeline facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:18:22Z"
    }
  ]
}
```
