# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/620
- Title: Celebrating the 60th anniversary of Medicaid.
- Congress: 119
- Bill type: HRES
- Bill number: 620
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-09-11T17:19:27Z
- Update date including text: 2025-09-11T17:19:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-29 - IntroReferral: Submitted in House
- Latest action: 2025-07-29: Submitted in House

## Actions

- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/620",
    "number": "620",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Celebrating the 60th anniversary of Medicaid.",
    "type": "HRES",
    "updateDate": "2025-09-11T17:19:27Z",
    "updateDateIncludingText": "2025-09-11T17:19:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:01:20Z",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "IA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres620ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 620\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Evans of Colorado (for himself, Mrs. Miller-Meeks , and Mr. Kean ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nCelebrating the 60th anniversary of Medicaid.\nThat the House of Representatives\u2014\n**(1)**\ncelebrates the 60th anniversary of Medicaid; and\n**(2)**\nwill continue to protect Medicaid from waste, fraud, and abuse to ensure its longevity for the most vulnerable Americans such as children, single mothers, the disabled, and individuals living below the Federal poverty line.",
      "versionDate": "2025-07-29",
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
        "updateDate": "2025-09-11T17:19:26Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres620ih.xml"
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
      "title": "Celebrating the 60th anniversary of Medicaid.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T13:03:24Z"
    },
    {
      "title": "Celebrating the 60th anniversary of Medicaid.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:35Z"
    }
  ]
}
```
