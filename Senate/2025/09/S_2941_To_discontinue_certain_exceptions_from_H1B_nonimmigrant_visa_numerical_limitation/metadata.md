# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2941?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2941
- Title: Visa Cap Enforcement Act
- Congress: 119
- Bill type: S
- Bill number: 2941
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2025-12-10T18:53:57Z
- Update date including text: 2025-12-10T18:53:57Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2941",
    "number": "2941",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Visa Cap Enforcement Act",
    "type": "S",
    "updateDate": "2025-12-10T18:53:57Z",
    "updateDateIncludingText": "2025-12-10T18:53:57Z"
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
          "date": "2025-09-30T15:32:58Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2941is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2941\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo discontinue certain exceptions from H\u20131B nonimmigrant visa numerical limitation.\n#### 1. Short title\nThis Act may be cited as the Visa Cap Enforcement Act .\n#### 2. Termination of certain exceptions from H\u20131B nonimmigrant visa numerical limitation\n##### (a) Three-Year period\nSection 214(g)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1184(g)(4) ) is amended by adding at the end the following: An alien who has been counted against the numerical limitation under paragraph (1)(A) shall be recounted against such numerical limitation during the fiscal year in which such alien surpasses 3 years in the nonimmigrant status described in section 101(a)(15)(H)(i)(b). .\n##### (b) Employment by colleges and research institutions\nSection 214(g) of the Immigration and Nationality Act ( 8 U.S.C. 1184(g) ) is amended by striking paragraph (5).\n##### (c) Change of status to H\u20131B nonimmigrant\nSection 214(l)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1184(l)(2)(A) ) is amended by striking the second sentence.\n##### (d) Change of employer\nSection 214(n)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1184(n)(1) ) is amended by inserting If the new position is approved, such position shall be counted against the numerical limitation under subsection (g)(1)(A). after the new petition is adjudicated. .",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-12-10T18:53:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2941is.xml"
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
      "title": "Visa Cap Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Visa Cap Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to discontinue certain exceptions from H-1B nonimmigrant visa numerical limitation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:24Z"
    }
  ]
}
```
