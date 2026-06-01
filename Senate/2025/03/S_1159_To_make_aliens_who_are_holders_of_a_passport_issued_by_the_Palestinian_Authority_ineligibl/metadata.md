# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1159?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1159
- Title: GAZA Act
- Congress: 119
- Bill type: S
- Bill number: 1159
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1159",
    "number": "1159",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "GAZA Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T21:03:09Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1159is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1159\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Daines introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo make aliens who are holders of a passport issued by the Palestinian Authority ineligible for visas, admission, or parole into the United States.\n#### 1. Short titles\nThis Act may be cited as the Guaranteeing Aggressors Zero Admission Act or the GAZA Act .\n#### 2. Ineligibility for visas, admission, or parole\nAn alien who is holder of a passport issued by the Palestinian Authority\u2014\n**(1)**\nis inadmissible to the United States;\n**(2)**\nis ineligible to receive a visa or other documentation to enter the United States; and\n**(3)**\nis otherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-04-11T12:26:11Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1159is.xml"
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
      "title": "GAZA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GAZA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guaranteeing Aggressors Zero Admission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to make aliens who are holders of a passport issued by the Palestinian Authority ineligible for visas, admission, or parole into the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:20Z"
    }
  ]
}
```
