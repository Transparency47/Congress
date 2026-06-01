# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/499?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/499
- Title: A resolution supporting the goals and ideals of "Creutzfeldt-Jakob Disease (CJD) Awareness Day".
- Congress: 119
- Bill type: SRES
- Bill number: 499
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2026-03-30T18:53:39Z
- Update date including text: 2026-03-30T18:53:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8207)
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8207)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/499",
    "number": "499",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A resolution supporting the goals and ideals of \"Creutzfeldt-Jakob Disease (CJD) Awareness Day\".",
    "type": "SRES",
    "updateDate": "2026-03-30T18:53:39Z",
    "updateDateIncludingText": "2026-03-30T18:53:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8207)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-11-18T22:12:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres499is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 499\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Husted submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nSupporting the goals and ideals of Creutzfeldt-Jakob Disease (CJD) Awareness Day .\nThat the Senate\u2014\n**(1)**\nsupports the goals and ideals of Creutzfeldt-Jakob Disease (CJD) Awareness Day ; and\n**(2)**\nrecognizes the importance of raising awareness of this rare brain disorder.",
      "versionDate": "2025-11-18",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-10",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "872",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the goals and ideals of \"Creutzfeldt-Jakob Disease (CJD) Awareness Day\".",
      "type": "HRES"
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
        "updateDate": "2025-11-21T13:13:06Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres499is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution supporting the goals and ideals of \"Creutzfeldt-Jakob Disease (CJD) Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-20T05:33:19Z"
    },
    {
      "title": "A resolution supporting the goals and ideals of \"Creutzfeldt-Jakob Disease (CJD) Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T11:56:19Z"
    }
  ]
}
```
