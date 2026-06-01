# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3484?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3484
- Title: A bill to amend section 3634 of title 18, United States Code, to extend the period for First Step Act reports.
- Congress: 119
- Bill type: S
- Bill number: 3484
- Origin chamber: Senate
- Introduced date: 2025-12-15
- Update date: 2026-01-12T16:04:14Z
- Update date including text: 2026-01-12T16:04:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in Senate
- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S8737)
- Latest action: 2025-12-15: Introduced in Senate

## Actions

- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S8737)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3484",
    "number": "3484",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A bill to amend section 3634 of title 18, United States Code, to extend the period for First Step Act reports.",
    "type": "S",
    "updateDate": "2026-01-12T16:04:14Z",
    "updateDateIncludingText": "2026-01-12T16:04:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S8737)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-16T00:04:25Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3484is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3484\nIN THE SENATE OF THE UNITED STATES\nDecember 15, 2025 Mr. Durbin (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 3634 of title 18, United States Code, to extend the period for First Step Act reports.\n#### 1. First Step Act reports\nSection 3634 of title 18, United States Code, is amended, in the matter preceding paragraph (1), by striking 5 years and inserting 10 years .",
      "versionDate": "2025-12-15",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-12T16:04:14Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3484is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 3634 of title 18, United States Code, to extend the period for First Step Act reports.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T03:18:15Z"
    },
    {
      "title": "A bill to amend section 3634 of title 18, United States Code, to extend the period for First Step Act reports.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T11:56:18Z"
    }
  ]
}
```
