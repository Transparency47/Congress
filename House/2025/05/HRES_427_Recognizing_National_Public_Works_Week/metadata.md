# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/427
- Title: Recognizing "National Public Works Week".
- Congress: 119
- Bill type: HRES
- Bill number: 427
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2025-11-19T20:25:29Z
- Update date including text: 2025-11-19T20:25:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-19 - IntroReferral: Submitted in House
- 2025-05-19 - IntroReferral: Submitted in House
- Latest action: 2025-05-19: Submitted in House

## Actions

- 2025-05-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/427",
    "number": "427",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Recognizing \"National Public Works Week\".",
    "type": "HRES",
    "updateDate": "2025-11-19T20:25:29Z",
    "updateDateIncludingText": "2025-11-19T20:25:29Z"
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
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
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
          "date": "2025-05-19T16:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres427ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 427\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Ms. Craig (for herself, Mr. Van Drew , and Ms. Titus ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nRecognizing National Public Works Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports National Public Works Week ; and\n**(2)**\nencourages the people of the United States to pay tribute to public works professionals, public works first responders, and those serving in support roles within the public works industry, to recognize the substantial contributions they make in protecting the country\u2019s health, safety, and quality of life.",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-23T18:21:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres427ih.xml"
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
      "title": "Recognizing \"National Public Works Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T08:18:49Z"
    },
    {
      "title": "Recognizing \"National Public Works Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T08:05:55Z"
    }
  ]
}
```
