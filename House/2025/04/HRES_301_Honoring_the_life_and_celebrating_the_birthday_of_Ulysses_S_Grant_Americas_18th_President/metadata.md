# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/301
- Title: Honoring the life and celebrating the birthday of Ulysses S. Grant, America's 18th President and native son of Ohio's Second Congressional District.
- Congress: 119
- Bill type: HRES
- Bill number: 301
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-06-06T14:17:56Z
- Update date including text: 2025-06-06T14:17:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-04-08 - IntroReferral: Submitted in House
- 2025-04-08 - IntroReferral: Submitted in House
- Latest action: 2025-04-08: Submitted in House

## Actions

- 2025-04-08 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-04-08 - IntroReferral: Submitted in House
- 2025-04-08 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/301",
    "number": "301",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Honoring the life and celebrating the birthday of Ulysses S. Grant, America's 18th President and native son of Ohio's Second Congressional District.",
    "type": "HRES",
    "updateDate": "2025-06-06T14:17:56Z",
    "updateDateIncludingText": "2025-06-06T14:17:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres301ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 301\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Taylor submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nHonoring the life and celebrating the birthday of Ulysses S. Grant, America\u2019s 18th President and native son of Ohio\u2019s Second Congressional District.\nThat the House of Representatives\u2014\n**(1)**\nhonors Ulysses S. Grant and the Land of US Grant, Inc., for their many contributions to Ohio and Ohio\u2019s Second Congressional District; and\n**(2)**\nrecognizes that Ulysses S. Grant was pivotal to the Union\u2019s military success in the Civil War and affirms his legacy as a trailblazer for civil rights and Reconstruction efforts.",
      "versionDate": "2025-04-08",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-22T00:54:02Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres301ih.xml"
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
      "title": "Honoring the life and celebrating the birthday of Ulysses S. Grant, America's 18th President and native son of Ohio's Second Congressional District.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T08:18:15Z"
    },
    {
      "title": "Honoring the life and celebrating the birthday of Ulysses S. Grant, America's 18th President and native son of Ohio's Second Congressional District.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T08:06:29Z"
    }
  ]
}
```
