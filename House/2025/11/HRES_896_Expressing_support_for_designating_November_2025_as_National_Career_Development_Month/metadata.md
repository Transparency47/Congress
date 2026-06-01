# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/896
- Title: Expressing support for designating November 2025 as "National Career Development Month".
- Congress: 119
- Bill type: HRES
- Bill number: 896
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2025-11-24T18:14:05Z
- Update date including text: 2025-11-24T18:14:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-11-19 - IntroReferral: Submitted in House
- 2025-11-19 - IntroReferral: Submitted in House
- Latest action: 2025-11-19: Submitted in House

## Actions

- 2025-11-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-11-19 - IntroReferral: Submitted in House
- 2025-11-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/896",
    "number": "896",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Expressing support for designating November 2025 as \"National Career Development Month\".",
    "type": "HRES",
    "updateDate": "2025-11-24T18:14:05Z",
    "updateDateIncludingText": "2025-11-24T18:14:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:01:20Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres896ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 896\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Thompson of Pennsylvania (for himself and Ms. Bonamici ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for designating November 2025 as National Career Development Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Career Development Month ;\n**(2)**\naffirms that career professionals are a valuable resource for the Nation\u2019s workforce;\n**(3)**\nrecognizes career development activities increase competencies needed for success in a global economy;\n**(4)**\nurges workers and jobseekers to utilize the services of career professionals; and\n**(5)**\nencourages career professionals, students, educators, parents, employers, and the current workforce to celebrate and promote career development.",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-11-24T18:14:05Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres896ih.xml"
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
      "title": "Expressing support for designating November 2025 as \"National Career Development Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T05:18:17Z"
    },
    {
      "title": "Expressing support for designating November 2025 as \"National Career Development Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T09:06:21Z"
    }
  ]
}
```
