# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/507?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/507
- Title: Expressing support for the designation of June 10 as "FSGS Awareness Day".
- Congress: 119
- Bill type: HRES
- Bill number: 507
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-06-27T13:16:52Z
- Update date including text: 2025-06-27T13:16:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-12 - IntroReferral: Submitted in House
- 2025-06-12 - IntroReferral: Submitted in House
- Latest action: 2025-06-12: Submitted in House

## Actions

- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-12 - IntroReferral: Submitted in House
- 2025-06-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/507",
    "number": "507",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Expressing support for the designation of June 10 as \"FSGS Awareness Day\".",
    "type": "HRES",
    "updateDate": "2025-06-27T13:16:52Z",
    "updateDateIncludingText": "2025-06-27T13:16:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:04:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres507ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 507\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Bilirakis submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of June 10 as FSGS Awareness Day .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of FSGS Awareness Day ;\n**(2)**\napplauds the efforts of advocates and organizations that encourage awareness, promote research, and provide education, support, and hope to those impacted by FSGS, including those suffering from recurrent FSGS; and\n**(3)**\nrecognizes the commitment of parents, families, researchers, health professionals, industry, and others dedicated to finding an effective treatment and eventual cure for FSGS.",
      "versionDate": "2025-06-12",
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
        "updateDate": "2025-06-27T13:16:52Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres507ih.xml"
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
      "title": "Expressing support for the designation of June 10 as \"FSGS Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T12:48:17Z"
    },
    {
      "title": "Expressing support for the designation of June 10 as \"FSGS Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T08:06:28Z"
    }
  ]
}
```
