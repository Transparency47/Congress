# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/835?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/835
- Title: Declaring gun violence a public health crisis.
- Congress: 119
- Bill type: HRES
- Bill number: 835
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-12-02T16:40:50Z
- Update date including text: 2025-12-02T16:40:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-10-28 - IntroReferral: Submitted in House
- 2025-10-28 - IntroReferral: Submitted in House
- Latest action: 2025-10-28: Submitted in House

## Actions

- 2025-10-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-10-28 - IntroReferral: Submitted in House
- 2025-10-28 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/835",
    "number": "835",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Declaring gun violence a public health crisis.",
    "type": "HRES",
    "updateDate": "2025-12-02T16:40:50Z",
    "updateDateIncludingText": "2025-12-02T16:40:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:00:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres835ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 835\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Espaillat submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nDeclaring gun violence a public health crisis.\nThat the House of Representatives\u2014\n**(1)**\ndeclares gun violence a public health crisis in the United States;\n**(2)**\nsupports the resolutions drafted, introduced, and adopted by cities, localities, and States across the Nation declaring gun violence a public health crisis or emergency;\n**(3)**\nurges a coordinated whole-of-government effort to addressing the gun violence public health crisis and ensuring the safety of all children;\n**(4)**\nurges the Centers for Disease Control and Prevention to continue its work utilizing the four-step public health approach to violence prevention and collaborate with other Federal Government agencies to resolve the gun violence public health crisis;\n**(5)**\nurges the Centers for Disease Control and Prevention to expand its research and data collection capabilities pertaining to gun violence prevention;\n**(6)**\nurges the Surgeon General to issue a report on firearm injuries and violence prevention; and\n**(7)**\ncommits to ending the gun violence public health crisis so that all people can enjoy life, liberty, and the pursuit of happiness.",
      "versionDate": "2025-10-28",
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
        "updateDate": "2025-12-02T16:40:50Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres835ih.xml"
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
      "title": "Declaring gun violence a public health crisis.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T08:18:52Z"
    },
    {
      "title": "Declaring gun violence a public health crisis.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T08:05:58Z"
    }
  ]
}
```
