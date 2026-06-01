# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1117
- Title: Expressing support for the designation of March as "Multiple System Atrophy Awareness Month" to strengthen public awareness of this neurodegenerative disorder.
- Congress: 119
- Bill type: HRES
- Bill number: 1117
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-03-19T15:25:24Z
- Update date including text: 2026-03-19T15:25:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-16 - IntroReferral: Submitted in House
- 2026-03-16 - IntroReferral: Submitted in House
- Latest action: 2026-03-16: Submitted in House

## Actions

- 2026-03-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-16 - IntroReferral: Submitted in House
- 2026-03-16 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1117",
    "number": "1117",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of March as \"Multiple System Atrophy Awareness Month\" to strengthen public awareness of this neurodegenerative disorder.",
    "type": "HRES",
    "updateDate": "2026-03-19T15:25:24Z",
    "updateDateIncludingText": "2026-03-19T15:25:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1117ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1117\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Mullin submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of March as Multiple System Atrophy Awareness Month to strengthen public awareness of this neurodegenerative disorder.\nThat the House of Representatives supports the designation of Multiple System Atrophy Awareness Month to strengthen public awareness of this neurodegenerative disorder and supports funding for research related to Multiple System Atrophy in hopes of developing therapeutics and treatments.",
      "versionDate": "2026-03-16",
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
        "name": "Health",
        "updateDate": "2026-03-19T15:25:24Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1117ih.xml"
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
      "title": "Expressing support for the designation of March as \"Multiple System Atrophy Awareness Month\" to strengthen public awareness of this neurodegenerative disorder.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T08:18:23Z"
    },
    {
      "title": "Expressing support for the designation of March as \"Multiple System Atrophy Awareness Month\" to strengthen public awareness of this neurodegenerative disorder.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T08:05:34Z"
    }
  ]
}
```
