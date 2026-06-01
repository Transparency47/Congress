# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1113
- Title: Censuring Representative Andrew Ogles and Removing Him from the House Committee on Homeland Security.
- Congress: 119
- Bill type: HRES
- Bill number: 1113
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-03-16T12:21:10Z
- Update date including text: 2026-03-16T12:21:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House
- Latest action: 2026-03-12: Submitted in House

## Actions

- 2026-03-12 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1113",
    "number": "1113",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Censuring Representative Andrew Ogles and Removing Him from the House Committee on Homeland Security.",
    "type": "HRES",
    "updateDate": "2026-03-16T12:21:10Z",
    "updateDateIncludingText": "2026-03-16T12:21:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:33:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1113ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1113\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Thanedar submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Andrew Ogles and Removing Him from the House Committee on Homeland Security.\n#### 1.\nCENSURE OF REPRESENTATIVE ANDREW OGLES.\nThat the House of Representatives\u2014\n**(1)**\nRepresentative Andrew Ogles be censured;\n**(2)**\nRepresentative Andrew Ogles forthwith present himself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\nRepresentative Andrew Ogles be censured with the public reading of this resolution by the Speaker.\n#### 2.\nREMOVAL FROM HOUSE COMMITTEE ON HOMELAND SECURITY.\nThe following named Member be, and is hereby, removed from the following standing committee of the House of Representatives:\nCommittee on Homeland Security:\nMr. Ogles.",
      "versionDate": "2026-03-12",
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
        "updateDate": "2026-03-16T12:21:09Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1113ih.xml"
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
      "title": "Censuring Representative Andrew Ogles and Removing Him from the House Committee on Homeland Security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:26Z"
    },
    {
      "title": "Censuring Representative Andrew Ogles and Removing Him from the House Committee on Homeland Security.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:05:38Z"
    }
  ]
}
```
