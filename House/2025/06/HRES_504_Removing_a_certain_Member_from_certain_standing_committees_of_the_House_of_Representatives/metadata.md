# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/504?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/504
- Title: Removing a certain Member from certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 504
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-06-26T14:43:29Z
- Update date including text: 2025-06-26T14:43:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House
- Latest action: 2025-06-11: Submitted in House

## Actions

- 2025-06-11 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/504",
    "number": "504",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Removing a certain Member from certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-06-26T14:43:29Z",
    "updateDateIncludingText": "2025-06-26T14:43:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:04:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres504ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 504\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mrs. Luna submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nRemoving a certain Member from certain standing committees of the House of Representatives.\nThat the following named Member be, and is hereby, removed from the following standing committees of the House of Representatives:\nCommittee on Homeland Security:\nMrs. McIver.\nCommittee on Small Business:\nMrs. McIver.",
      "versionDate": "2025-06-11",
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
        "name": "Congress",
        "updateDate": "2025-06-26T14:43:29Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres504ih.xml"
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
      "title": "Removing a certain Member from certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T08:18:26Z"
    },
    {
      "title": "Removing a certain Member from certain standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:07:09Z"
    }
  ]
}
```
