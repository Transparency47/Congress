# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2942?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2942
- Title: A bill for the relief of Valent Kolami.
- Congress: 119
- Bill type: S
- Bill number: 2942
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2025-12-08T18:18:12Z
- Update date including text: 2025-12-08T18:18:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2942",
    "number": "2942",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A bill for the relief of Valent Kolami.",
    "type": "S",
    "updateDate": "2025-12-08T18:18:12Z",
    "updateDateIncludingText": "2025-12-08T18:18:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:19:07Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2942is.xml",
      "text": "VI\n119th CONGRESS\n1st Session\nS. 2942\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Blumenthal introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nFor the relief of Valent Kolami.\n#### 1. Permanent resident status for Valent Kolami\n##### (a) In general\nNotwithstanding subsections (a) and (b) of section 201 of the Immigration and Nationality Act ( 8 U.S.C. 1151 ), Valent Kolami shall be eligible for issuance of an immigrant visa or for adjustment of status to that of an alien lawfully admitted for permanent residence upon filing an application for issuance of an immigrant visa under section 204 of such Act ( 8 U.S.C. 1154 ) or for adjustment of status to lawful permanent resident.\n##### (b) Adjustment of status\nIf Valent Kolami enters the United States before the filing deadline specified in subsection (c), Valent Kolami shall be considered to have entered and remained lawfully in the United States and shall be eligible for adjustment of status under section 245 of the Immigration and Nationality Act ( 8 U.S.C. 1255 ) as of the date of the enactment of this Act.\n##### (c) Application and payment of fees\nSubsections (a) and (b) shall apply only if the application for the issuance of an immigrant visa or the application for adjustment of status is filed with appropriate fees not later than 2 years after the date of the enactment of this Act.\n##### (d) PAYGO\nThe budgetary effects of this Act, for the purpose of complying with the Statutory Pay-As-You-Go Act of 2010, shall be determined by reference to the latest statement titled Budgetary Effects of PAYGO Legislation for this Act, submitted for printing in the Congressional Record by the Chairman of the Senate Budget Committee, provided that such statement has been submitted prior to the vote on passage.",
      "versionDate": "2025-09-30",
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
      "legislativeSubjects": {
        "item": {
          "name": "Private Legislation",
          "updateDate": "2025-12-08T18:18:12Z"
        }
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2942is.xml"
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
      "title": "A bill for the relief of Valent Kolami.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:37Z"
    },
    {
      "title": "A bill for the relief of Valent Kolami.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T10:56:16Z"
    }
  ]
}
```
