# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3334
- Title: LAB Personnel Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3334
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-01-07T17:33:07Z
- Update date including text: 2026-01-07T17:33:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3334",
    "number": "3334",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "LAB Personnel Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T17:33:07Z",
    "updateDateIncludingText": "2026-01-07T17:33:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T21:24:21Z",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3334is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3334\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mrs. Shaheen (for herself and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit reductions in the workforce at the Drug Enforcement Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Laboratory Analysts and Biometric Personnel Act of 2025 or the LAB Personnel Act of 2025 .\n#### 2. Definition\nIn this Act, the term laboratory workforce at the Drug Enforcement Administration means\u2014\n**(1)**\npositions in the Drug Enforcement Administration at forensic laboratories of the Drug Enforcement Administration, including\u2014\n**(A)**\nforensic chemists;\n**(B)**\nfingerprint specialists;\n**(C)**\ndigital forensic examiners; and\n**(D)**\nany other positions in the Drug Enforcement Administration at such forensic laboratories; and\n**(2)**\nother positions in the Drug Enforcement Administration at locations other than such a forensic laboratory that will be relocated to such a forensic laboratory that, as of the date of the enactment of this Act, is being constructed or otherwise finalized.\n#### 3. Prohibition on reducing the laboratory workforce at the Drug Enforcement Agency\n##### (a) In general\nThe laboratory workforce at the Drug Enforcement Administration shall be exempt from any hiring freezes or workforce reductions related to spending cuts, reprogramming of funds, or the probationary status of employees.\n##### (b) Rule of construction\nNothing in this section may be construed to restrict the authority of the Attorney General to manage the workforce of the Department of Justice under existing procedures in cases of misconduct or poor performance.",
      "versionDate": "2025-12-03",
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
        "actionDate": "2025-11-18",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6103",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LAB Personnel Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-07T17:33:06Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3334is.xml"
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
      "title": "LAB Personnel Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LAB Personnel Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Laboratory Analysts and Biometric Personnel Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit reductions in the workforce at the Drug Enforcement Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:22Z"
    }
  ]
}
```
