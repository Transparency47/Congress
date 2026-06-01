# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/299
- Title: Expressing support for the designation of July 2025 as Veterans Appreciation Month.
- Congress: 119
- Bill type: HRES
- Bill number: 299
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-05-22T00:48:30Z
- Update date including text: 2025-05-22T00:48:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-07 - IntroReferral: Submitted in House
- 2025-04-07 - IntroReferral: Submitted in House
- Latest action: 2025-04-07: Submitted in House

## Actions

- 2025-04-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-07 - IntroReferral: Submitted in House
- 2025-04-07 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/299",
    "number": "299",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Expressing support for the designation of July 2025 as Veterans Appreciation Month.",
    "type": "HRES",
    "updateDate": "2025-05-22T00:48:30Z",
    "updateDateIncludingText": "2025-05-22T00:48:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-07T16:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres299ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 299\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Van Drew submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of July 2025 as Veterans Appreciation Month.\nThat the House of Representatives supports the designation of Veterans Appreciation Month.",
      "versionDate": "2025-04-07",
      "versionType": "IH"
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
        "updateDate": "2025-05-22T00:48:30Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres299ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the designation of July 2025 as Veterans Appreciation Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T10:48:18Z"
    },
    {
      "title": "Expressing support for the designation of July 2025 as Veterans Appreciation Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T08:06:22Z"
    }
  ]
}
```
