# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/123?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/123
- Title: Congratulating the Philadelphia Eagles on their victory in Super Bowl LIX.
- Congress: 119
- Bill type: HRES
- Bill number: 123
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-02-14T15:53:08Z
- Update date including text: 2025-02-14T15:53:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-10 - Committee: Submitted in House
- 2025-02-11 - IntroReferral: Sponsor introductory remarks on measure. (CR H622)
- Latest action: 2025-02-10: Submitted in House

## Actions

- 2025-02-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-10 - Committee: Submitted in House
- 2025-02-11 - IntroReferral: Sponsor introductory remarks on measure. (CR H622)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/123",
    "number": "123",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "B001296",
        "district": "2",
        "firstName": "Brendan",
        "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
        "lastName": "Boyle",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Congratulating the Philadelphia Eagles on their victory in Super Bowl LIX.",
    "type": "HRES",
    "updateDate": "2025-02-14T15:53:08Z",
    "updateDateIncludingText": "2025-02-14T15:53:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H622)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-10T17:01:05Z",
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
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NJ"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres123ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 123\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Boyle of Pennsylvania (for himself, Mr. Evans of Pennsylvania , Mr. Norcross , Ms. Scanlon , Ms. Dean of Pennsylvania , Mr. Fitzpatrick , and Ms. Houlahan ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCongratulating the Philadelphia Eagles on their victory in Super Bowl LIX.\nThat the House of Representatives\u2014\n**(1)**\ncongratulates the Philadelphia Eagles on their hard-fought victory in Super Bowl LIX; and\n**(2)**\nrecognizes the achievements of all the players, coaches, and staff who contributed to the victory.",
      "versionDate": "2025-02-10",
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
        "name": "Sports and Recreation",
        "updateDate": "2025-02-14T15:53:08Z"
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
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres123ih.xml"
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
      "title": "Congratulating the Philadelphia Eagles on their victory in Super Bowl LIX.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T09:03:33Z"
    },
    {
      "title": "Congratulating the Philadelphia Eagles on their victory in Super Bowl LIX.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T09:00:28Z"
    }
  ]
}
```
