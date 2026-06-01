# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/272
- Title: Expressing the sense of the House of Representatives that the United States seeks to restore peace in Ukraine.
- Congress: 119
- Bill type: HRES
- Bill number: 272
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-05-21T17:32:46Z
- Update date including text: 2025-05-21T17:32:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Submitted in House
- Latest action: 2025-03-31: Submitted in House

## Actions

- 2025-03-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/272",
    "number": "272",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that the United States seeks to restore peace in Ukraine.",
    "type": "HRES",
    "updateDate": "2025-05-21T17:32:46Z",
    "updateDateIncludingText": "2025-05-21T17:32:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres272ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 272\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Davidson submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nExpressing the sense of the House of Representatives that the United States seeks to restore peace in Ukraine.\nThat the House of Representatives expresses\u2014\n**(1)**\nsupport for the Trump administration\u2019s efforts to restore peace between Ukraine and Russia without expanding or escalating the war; and\n**(2)**\nthat\u2014\n**(A)**\nthe United States should not expend any more money, resources, or manpower participating in the Russia-Ukraine War;\n**(B)**\nall military advisors, intelligence assets, and involved government personnel should withdraw from participation in the war;\n**(C)**\nthe United States Government should put America first and secure our own borders instead of those of far-off countries; and\n**(D)**\nthe United States should cease all intelligence sharing with the Ukrainian Government, as well as all involved European intelligence agencies that leak shared United States intelligence in contravention of this resolution.",
      "versionDate": "2025-03-31",
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
        "name": "International Affairs",
        "updateDate": "2025-05-21T17:32:46Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres272ih.xml"
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
      "title": "Expressing the sense of the House of Representatives that the United States seeks to restore peace in Ukraine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T13:18:25Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives that the United States seeks to restore peace in Ukraine.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T08:06:41Z"
    }
  ]
}
```
