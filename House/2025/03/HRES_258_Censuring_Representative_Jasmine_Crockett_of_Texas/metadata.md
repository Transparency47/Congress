# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/258
- Title: Censuring Representative Jasmine Crockett of Texas.
- Congress: 119
- Bill type: HRES
- Bill number: 258
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-05-09T15:51:20Z
- Update date including text: 2025-05-09T15:51:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-03-26 - IntroReferral: Submitted in House
- 2025-03-26 - IntroReferral: Submitted in House
- Latest action: 2025-03-26: Submitted in House

## Actions

- 2025-03-26 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-03-26 - IntroReferral: Submitted in House
- 2025-03-26 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/258",
    "number": "258",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Censuring Representative Jasmine Crockett of Texas.",
    "type": "HRES",
    "updateDate": "2025-05-09T15:51:20Z",
    "updateDateIncludingText": "2025-05-09T15:51:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres258ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 258\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Weber of Texas (for himself and Mr. Carter of Texas ) submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Jasmine Crockett of Texas.\nThat\u2014\n**(1)**\nRepresentative Jasmine Crockett of Texas be censured;\n**(2)**\nRepresentative Jasmine Crockett forthwith present herself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\nRepresentative Jasmine Crockett be censured with the public reading of this resolution by the Speaker.",
      "versionDate": "2025-03-26",
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
        "name": "Congress",
        "updateDate": "2025-05-09T15:51:20Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres258ih.xml"
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
      "title": "Censuring Representative Jasmine Crockett of Texas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T08:18:22Z"
    },
    {
      "title": "Censuring Representative Jasmine Crockett of Texas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T08:06:09Z"
    }
  ]
}
```
