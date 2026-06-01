# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/766?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/766
- Title: Celebrating the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture.
- Congress: 119
- Bill type: HRES
- Bill number: 766
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-09-29T13:54:26Z
- Update date including text: 2025-09-29T13:54:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-26 - IntroReferral: Submitted in House
- 2025-09-26 - IntroReferral: Submitted in House
- Latest action: 2025-09-26: Submitted in House

## Actions

- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-26 - IntroReferral: Submitted in House
- 2025-09-26 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/766",
    "number": "766",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
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
    "title": "Celebrating the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture.",
    "type": "HRES",
    "updateDate": "2025-09-29T13:54:26Z",
    "updateDateIncludingText": "2025-09-29T13:54:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres766ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 766\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Espaillat submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCelebrating the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture;\n**(2)**\ncommends the critical work it has done in advancing intellectual growth, cultural understanding, and historical preservation of African and Black culture; and\n**(3)**\ncelebrates the lasting and continued impact of the Schomberg Center as a beacon of research, creativity, and community engagement in African-American and African Diaspora studies, and American history.",
      "versionDate": "2025-09-26",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-09-29T13:54:26Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres766ih.xml"
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
      "title": "Celebrating the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T08:18:18Z"
    },
    {
      "title": "Celebrating the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T08:06:05Z"
    }
  ]
}
```
