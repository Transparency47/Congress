# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/745
- Title: Expressing support for the designation of October 1 as "National Latino and Latina Physician Day".
- Congress: 119
- Bill type: HRES
- Bill number: 745
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-10-25T08:05:13Z
- Update date including text: 2025-10-25T08:05:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-18 - IntroReferral: Submitted in House
- 2025-09-18 - IntroReferral: Submitted in House
- Latest action: 2025-09-18: Submitted in House

## Actions

- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-18 - IntroReferral: Submitted in House
- 2025-09-18 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/745",
    "number": "745",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of October 1 as \"National Latino and Latina Physician Day\".",
    "type": "HRES",
    "updateDate": "2025-10-25T08:05:13Z",
    "updateDateIncludingText": "2025-10-25T08:05:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:02:40Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres745ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 745\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Ruiz (for himself and Ms. Salazar ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of October 1 as National Latino and Latina Physician Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals of increasing the number of Latino and Latina physicians in the United States and increasing diversity in the medical field; and\n**(2)**\nsupports the designation of National Latino and Latina Physician Day .",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-09-24T14:59:40Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres745ih.xml"
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
      "title": "Expressing support for the designation of October 1 as \"National Latino and Latina Physician Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T08:18:20Z"
    },
    {
      "title": "Expressing support for the designation of October 1 as \"National Latino and Latina Physician Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T08:07:13Z"
    }
  ]
}
```
