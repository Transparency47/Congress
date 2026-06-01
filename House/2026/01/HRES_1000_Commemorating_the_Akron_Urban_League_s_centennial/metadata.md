# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1000
- Title: Commemorating the Akron Urban League's centennial.
- Congress: 119
- Bill type: HRES
- Bill number: 1000
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-01-16T12:58:36Z
- Update date including text: 2026-01-16T12:58:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-14 - IntroReferral: Submitted in House
- 2026-01-14 - IntroReferral: Submitted in House
- Latest action: 2026-01-14: Submitted in House

## Actions

- 2026-01-14 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-14 - IntroReferral: Submitted in House
- 2026-01-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1000",
    "number": "1000",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Commemorating the Akron Urban League's centennial.",
    "type": "HRES",
    "updateDate": "2026-01-16T12:58:36Z",
    "updateDateIncludingText": "2026-01-16T12:58:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:03:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1000ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1000\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mrs. Sykes submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nCommemorating the Akron Urban League\u2019s centennial.\nThat the House of Representatives\u2014\n**(1)**\nhonors and commemorates the 100 years of work to empower communities, strengthen families, and open doors of opportunity by the Akron Urban League;\n**(2)**\nrecognizes the generational impact that the Akron Urban League has had on the city of Akron and the residents of Summit County; and\n**(3)**\nencourages the Akron Urban League to continue its mission to improve the quality of life of the citizens of Summit County, particularly African Americans, through economic self-reliance and social empowerment for another 100 years.",
      "versionDate": "2026-01-14",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-01-16T12:58:35Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1000ih.xml"
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
      "title": "Commemorating the Akron Urban League's centennial.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-15T10:48:18Z"
    },
    {
      "title": "Commemorating the Akron Urban League's centennial.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T09:06:46Z"
    }
  ]
}
```
