# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/429
- Title: Expressing support for the designation of May 17, 2025, as "Necrotizing Enterocolitis Awareness Day".
- Congress: 119
- Bill type: HRES
- Bill number: 429
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2025-05-27T15:30:07Z
- Update date including text: 2025-05-27T15:30:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-19 - IntroReferral: Submitted in House
- 2025-05-19 - IntroReferral: Submitted in House
- Latest action: 2025-05-19: Submitted in House

## Actions

- 2025-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-19 - IntroReferral: Submitted in House
- 2025-05-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/429",
    "number": "429",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of May 17, 2025, as \"Necrotizing Enterocolitis Awareness Day\".",
    "type": "HRES",
    "updateDate": "2025-05-27T15:30:07Z",
    "updateDateIncludingText": "2025-05-27T15:30:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T16:01:30Z",
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
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres429ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 429\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Mr. Thompson of California (for himself, Mr. Kiley of California , and Mr. McGarvey ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May 17, 2025, as Necrotizing Enterocolitis Awareness Day .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the importance of raising awareness about necrotizing enterocolitis; and\n**(2)**\nexpresses support for the designation of Necrotizing Enterocolitis Awareness Day .",
      "versionDate": "2025-05-19",
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
        "updateDate": "2025-05-27T15:30:07Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres429ih.xml"
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
      "title": "Expressing support for the designation of May 17, 2025, as \"Necrotizing Enterocolitis Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T08:18:48Z"
    },
    {
      "title": "Expressing support for the designation of May 17, 2025, as \"Necrotizing Enterocolitis Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T08:05:56Z"
    }
  ]
}
```
