# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/676
- Title: Censuring Representative Cory Mills.
- Congress: 119
- Bill type: HRES
- Bill number: 676
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2025-09-24T16:16:33Z
- Update date including text: 2025-09-24T16:16:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-09-03 - IntroReferral: Submitted in House
- 2025-09-03 - IntroReferral: Submitted in House
- Latest action: 2025-09-03: Submitted in House

## Actions

- 2025-09-03 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-09-03 - IntroReferral: Submitted in House
- 2025-09-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/676",
    "number": "676",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Censuring Representative Cory Mills.",
    "type": "HRES",
    "updateDate": "2025-09-24T16:16:33Z",
    "updateDateIncludingText": "2025-09-24T16:16:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:01:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres676ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 676\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Ms. Clarke of New York submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Cory Mills.\nThat\u2014\n**(1)**\nRepresentative Cory Mills be censured;\n**(2)**\nRepresentative Cory Mills forthwith present himself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\nRepresentative Cory Mills be censured with the public reading of this resolution by the Speaker.",
      "versionDate": "2025-09-03",
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
        "updateDate": "2025-09-24T16:16:33Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres676ih.xml"
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
      "title": "Censuring Representative Cory Mills.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-04T10:33:18Z"
    },
    {
      "title": "Censuring Representative Cory Mills.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-04T08:06:45Z"
    }
  ]
}
```
