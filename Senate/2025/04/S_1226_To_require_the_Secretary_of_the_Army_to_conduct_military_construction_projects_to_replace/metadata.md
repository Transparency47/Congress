# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1226
- Title: Restoring Fort Leonard Wood Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1226
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-05-22T00:44:34Z
- Update date including text: 2025-05-22T00:44:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1226",
    "number": "1226",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Restoring Fort Leonard Wood Act of 2025",
    "type": "S",
    "updateDate": "2025-05-22T00:44:34Z",
    "updateDateIncludingText": "2025-05-22T00:44:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T17:59:48Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1226is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1226\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Hawley introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of the Army to conduct military construction projects to replace military family housing units at Fort Leonard Wood, Missouri, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Fort Leonard Wood Act of 2025 .\n#### 2. Military construction projects to replace military family housing units at Fort Leonard Wood, Missouri\n##### (a) In general\nThe Secretary of the Army shall conduct a military construction project or military construction projects to replace 1,142 units of military family housing at Fort Leonard Wood, Missouri.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of the Army $700,000,000 to carry out subsection (a).",
      "versionDate": "2025-04-01",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-22T00:44:34Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1226is.xml"
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
      "title": "Restoring Fort Leonard Wood Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Fort Leonard Wood Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Army to conduct military construction projects to replace military family housing units at Fort Leonard Wood, Missouri, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:25Z"
    }
  ]
}
```
