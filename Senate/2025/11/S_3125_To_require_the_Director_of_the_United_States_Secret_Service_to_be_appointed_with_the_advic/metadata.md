# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3125
- Title: PROTECT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3125
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-19T13:29:25Z
- Update date including text: 2025-11-19T13:29:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3125",
    "number": "3125",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "PROTECT Act of 2025",
    "type": "S",
    "updateDate": "2025-11-19T13:29:25Z",
    "updateDateIncludingText": "2025-11-19T13:29:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T17:07:35Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3125is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3125\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Grassley (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Director of the United States Secret Service to be appointed with the advice and consent of the Senate.\n#### 1. Short title\nThis Act may be cited as the Providing Real Oversight and Transparency to Effectively Counter Threats Act of 2025 or the PROTECT Act of 2025 .\n#### 2. Senate confirmation\nSection 3056 of title 18, United States Code, is amended by adding at the end the following:\n(h) (1) The United States Secret Service shall be headed by a Director, who shall be appointed by the President, by and with the advice and consent of the Senate. (2) (A) With respect to the term of service of the Director of the United States Secret Service\u2014 (i) the term shall be 10 years; and (ii) an individual appointed as the Director may serve not more than 1 term. (B) Subparagraph (A) shall take effect on the date on which the President first appoints an individual as the Director of the United States Secret Service after the date of enactment of the Providing Real Oversight and Transparency to Effectively Counter Threats Act of 2025 . .",
      "versionDate": "2025-11-06",
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
        "updateDate": "2025-11-19T13:29:25Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3125is.xml"
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
      "title": "PROTECT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T06:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Real Oversight and Transparency to Effectively Counter Threats Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the United States Secret Service to be appointed with the advice and consent of the Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:23Z"
    }
  ]
}
```
