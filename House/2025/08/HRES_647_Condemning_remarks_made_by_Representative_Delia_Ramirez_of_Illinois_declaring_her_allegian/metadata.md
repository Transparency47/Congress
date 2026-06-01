# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/647
- Title: Condemning remarks made by Representative Delia Ramirez of Illinois declaring her allegiance to the Republic of Guatemala before the United States of America.
- Congress: 119
- Bill type: HRES
- Bill number: 647
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2025-09-11T20:53:40Z
- Update date including text: 2025-09-11T20:53:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-08-12 - IntroReferral: Submitted in House
- 2025-08-12 - IntroReferral: Submitted in House
- Latest action: 2025-08-12: Submitted in House

## Actions

- 2025-08-12 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-08-12 - IntroReferral: Submitted in House
- 2025-08-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/647",
    "number": "647",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Condemning remarks made by Representative Delia Ramirez of Illinois declaring her allegiance to the Republic of Guatemala before the United States of America.",
    "type": "HRES",
    "updateDate": "2025-09-11T20:53:40Z",
    "updateDateIncludingText": "2025-09-11T20:53:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres647ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 647\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Carter of Georgia submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCondemning remarks made by Representative Delia Ramirez of Illinois declaring her allegiance to the Republic of Guatemala before the United States of America.\nThat the House of Representatives\u2014\n**(1)**\ncondemns the anti-American comments made by Representative Delia Ramirez of Illinois;\n**(2)**\naffirms its allegiance to always put the interests of American citizens before those of other nations;\n**(3)**\ncondemns comments that put the interests of foreign nations above those of the United States; and\n**(4)**\naffirms its commitment to always put the safety, prosperity, and overall well-being of the American people first before those of other nations.",
      "versionDate": "2025-08-12",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-11T20:53:40Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres647ih.xml"
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
      "title": "Condemning remarks made by Representative Delia Ramirez of Illinois declaring her allegiance to the Republic of Guatemala before the United States of America.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:32Z"
    },
    {
      "title": "Condemning remarks made by Representative Delia Ramirez of Illinois declaring her allegiance to the Republic of Guatemala before the United States of America.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:05:33Z"
    }
  ]
}
```
