# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/686
- Title: Supporting the designation of the week of September 14, 2025, through September 20, 2025, as "Telehealth Awareness Week".
- Congress: 119
- Bill type: HRES
- Bill number: 686
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2025-09-23T17:33:24Z
- Update date including text: 2025-09-23T17:33:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-09 - IntroReferral: Submitted in House
- 2025-09-09 - IntroReferral: Submitted in House
- Latest action: 2025-09-09: Submitted in House

## Actions

- 2025-09-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-09 - IntroReferral: Submitted in House
- 2025-09-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/686",
    "number": "686",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Supporting the designation of the week of September 14, 2025, through September 20, 2025, as \"Telehealth Awareness Week\".",
    "type": "HRES",
    "updateDate": "2025-09-23T17:33:24Z",
    "updateDateIncludingText": "2025-09-23T17:33:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
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
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:00:20Z",
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
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AZ"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres686ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 686\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Mr. Carter of Georgia (for himself, Ms. Matsui , Mr. Schweikert , and Mr. Thompson of California ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the designation of the week of September 14, 2025, through September 20, 2025, as Telehealth Awareness Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Telehealth Awareness Week ;\n**(2)**\nrecognizes the impact of telehealth in delivering health care services to patients across the United States; and\n**(3)**\nurges that steps be taken to\u2014\n**(A)**\ncontinue the telehealth flexibilities beyond September 30, 2025;\n**(B)**\nraise awareness about the benefits of expanding telehealth;\n**(C)**\nhighlight resources for health care providers and patients regarding telehealth;\n**(D)**\ncollect and analyze data on the impacts of telehealth; and\n**(E)**\npromote continued access to telehealth for all communities and across settings permanently.",
      "versionDate": "2025-09-09",
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
        "updateDate": "2025-09-23T17:33:24Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres686ih.xml"
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
      "title": "Supporting the designation of the week of September 14, 2025, through September 20, 2025, as \"Telehealth Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-10T08:18:26Z"
    },
    {
      "title": "Supporting the designation of the week of September 14, 2025, through September 20, 2025, as \"Telehealth Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T08:06:13Z"
    }
  ]
}
```
