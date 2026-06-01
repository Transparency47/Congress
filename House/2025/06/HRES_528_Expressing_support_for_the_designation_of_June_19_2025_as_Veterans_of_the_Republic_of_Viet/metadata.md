# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/528
- Title: Expressing support for the designation of June 19, 2025, as "Veterans of the Republic of Vietnam Armed Forces Day".
- Congress: 119
- Bill type: HRES
- Bill number: 528
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2025-07-17T15:46:00Z
- Update date including text: 2025-07-17T15:46:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-07-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H3207)
- Latest action: 2025-06-20: Submitted in House

## Actions

- 2025-06-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-07-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H3207)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/528",
    "number": "528",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000491",
        "district": "45",
        "firstName": "Derek",
        "fullName": "Rep. Tran, Derek [D-CA-45]",
        "lastName": "Tran",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of June 19, 2025, as \"Veterans of the Republic of Vietnam Armed Forces Day\".",
    "type": "HRES",
    "updateDate": "2025-07-17T15:46:00Z",
    "updateDateIncludingText": "2025-07-17T15:46:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3207)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
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
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:01:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres528ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 528\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Mr. Tran submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nExpressing support for the designation of June 19, 2025, as Veterans of the Republic of Vietnam Armed Forces Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Veterans of the Republic of Vietnam Armed Forces Day , in remembrance of the soldiers who sacrificed their lives for freedom and democracy; and\n**(2)**\nhonors the victims, survivors, activists, and freedom fighters of the Vietnam war.",
      "versionDate": "2025-06-20",
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
        "updateDate": "2025-07-17T15:45:59Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres528ih.xml"
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
      "title": "Expressing support for the designation of June 19, 2025, as \"Veterans of the Republic of Vietnam Armed Forces Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T08:18:18Z"
    },
    {
      "title": "Expressing support for the designation of June 19, 2025, as \"Veterans of the Republic of Vietnam Armed Forces Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T08:05:28Z"
    }
  ]
}
```
