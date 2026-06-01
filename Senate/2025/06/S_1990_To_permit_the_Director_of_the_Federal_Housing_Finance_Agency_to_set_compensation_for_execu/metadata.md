# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1990?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1990
- Title: CURB Act
- Congress: 119
- Bill type: S
- Bill number: 1990
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-06-26T12:35:05Z
- Update date including text: 2025-06-26T12:35:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1990",
    "number": "1990",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "CURB Act",
    "type": "S",
    "updateDate": "2025-06-26T12:35:05Z",
    "updateDateIncludingText": "2025-06-26T12:35:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T22:29:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sponsorshipDate": "2025-06-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1990is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1990\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Mr. Banks (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo permit the Director of the Federal Housing Finance Agency to set compensation for executive officers of Federal Home Loan Banks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Curtailing Unreasonable Remuneration at Banks Act or the CURB Act .\n#### 2. Compensation for executive officers of Federal Home Loan Banks\nSection 7 of the Federal Home Loan Bank Act ( 12 U.S.C. 1427 ) is amended\u2014\n**(1)**\nin the first subsection (l) (relating to withholding of compensation)\u2014\n**(A)**\nin the subsection heading, by striking Withholding of compensation and inserting Compensation of executive officers ;\n**(B)**\nby striking Notwithstanding and inserting the following:\n(1) Withholding of compensation Notwithstanding ; and\n**(C)**\nby adding at the end the following:\n(1) Setting compensation Notwithstanding section 1318(d) of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4518(d) ), the Director may establish compensation for any executive officer of a Federal Home Loan Bank that is reasonable and comparable in accordance with regulations promulgated by the Director. ; and\n**(2)**\nby striking the second subsection (l) (relating to the transition rule).",
      "versionDate": "2025-06-09",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-06-26T12:35:05Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1990is.xml"
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
      "title": "CURB Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CURB Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Curtailing Unreasonable Remuneration at Banks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit the Director of the Federal Housing Finance Agency to set compensation for executive officers of Federal Home Loan Banks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T03:33:16Z"
    }
  ]
}
```
