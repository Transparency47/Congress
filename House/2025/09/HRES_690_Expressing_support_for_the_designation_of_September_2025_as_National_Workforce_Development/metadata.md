# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/690
- Title: Expressing support for the designation of September 2025 as "National Workforce Development Month".
- Congress: 119
- Bill type: HRES
- Bill number: 690
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-09-24T16:20:25Z
- Update date including text: 2025-09-24T16:20:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-09-10 - IntroReferral: Submitted in House
- 2025-09-10 - IntroReferral: Submitted in House
- Latest action: 2025-09-10: Submitted in House

## Actions

- 2025-09-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-09-10 - IntroReferral: Submitted in House
- 2025-09-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/690",
    "number": "690",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Expressing support for the designation of September 2025 as \"National Workforce Development Month\".",
    "type": "HRES",
    "updateDate": "2025-09-24T16:20:25Z",
    "updateDateIncludingText": "2025-09-24T16:20:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "KY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres690ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 690\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Ms. Bonamici (for herself, Mr. Guthrie , and Mr. Thompson of Pennsylvania ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of September 2025 as National Workforce Development Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Workforce Development Month ;\n**(2)**\nsupports Federal initiatives to promote workforce development; and\n**(3)**\nacknowledges that workforce development plays a crucial role in supporting workers, increasing labor force participation, and growing the economy.",
      "versionDate": "2025-09-10",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-24T16:20:25Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres690ih.xml"
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
      "title": "Expressing support for the designation of September 2025 as \"National Workforce Development Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T10:18:23Z"
    },
    {
      "title": "Expressing support for the designation of September 2025 as \"National Workforce Development Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:26Z"
    }
  ]
}
```
