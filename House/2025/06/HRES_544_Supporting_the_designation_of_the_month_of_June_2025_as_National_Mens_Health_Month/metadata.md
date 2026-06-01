# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/544
- Title: Supporting the designation of the month of June 2025, as "National Men's Health Month".
- Congress: 119
- Bill type: HRES
- Bill number: 544
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-07-09T13:10:01Z
- Update date including text: 2025-07-09T13:10:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-25 - IntroReferral: Submitted in House
- 2025-06-25 - IntroReferral: Submitted in House
- Latest action: 2025-06-25: Submitted in House

## Actions

- 2025-06-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-25 - IntroReferral: Submitted in House
- 2025-06-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/544",
    "number": "544",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "Supporting the designation of the month of June 2025, as \"National Men's Health Month\".",
    "type": "HRES",
    "updateDate": "2025-07-09T13:10:01Z",
    "updateDateIncludingText": "2025-07-09T13:10:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "GA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NJ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres544ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 544\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Carter of Louisiana (for himself, Mr. McCormick , Mr. Dunn of Florida , Mr. Menendez , and Mr. Lieu ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the designation of the month of June 2025, as National Men\u2019s Health Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the annual National Men\u2019s Health Month ; and\n**(2)**\nrequests that the President issue a proclamation calling upon the people of the United States and interested groups to observe National Men\u2019s Health Month with appropriate ceremonies and activities.",
      "versionDate": "2025-06-25",
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
        "updateDate": "2025-07-09T13:10:01Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres544ih.xml"
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
      "title": "Supporting the designation of the month of June 2025, as \"National Men's Health Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T08:48:35Z"
    },
    {
      "title": "Supporting the designation of the month of June 2025, as \"National Men's Health Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T08:06:23Z"
    }
  ]
}
```
