# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1012
- Title: Recognizing and honoring Cristina M. Rodríguez for her historic appointment as dean of Yale Law School.
- Congress: 119
- Bill type: HRES
- Bill number: 1012
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-01-26T14:53:55Z
- Update date including text: 2026-01-26T14:53:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-21 - IntroReferral: Submitted in House
- 2026-01-21 - IntroReferral: Submitted in House
- Latest action: 2026-01-21: Submitted in House

## Actions

- 2026-01-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-21 - IntroReferral: Submitted in House
- 2026-01-21 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1012",
    "number": "1012",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001091",
        "district": "20",
        "firstName": "Joaquin",
        "fullName": "Rep. Castro, Joaquin [D-TX-20]",
        "lastName": "Castro",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Recognizing and honoring Cristina M. Rodr\u00edguez for her historic appointment as dean of Yale Law School.",
    "type": "HRES",
    "updateDate": "2026-01-26T14:53:55Z",
    "updateDateIncludingText": "2026-01-26T14:53:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:00:50Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1012ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1012\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Castro of Texas (for himself and Ms. DeLauro ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing and honoring Cristina M. Rodr\u00edguez for her historic appointment as dean of Yale Law School.\nThat the House of Representatives\u2014\n**(1)**\nhonors Cristina M. Rodr\u00edguez for her landmark appointment as dean of Yale Law School;\n**(2)**\nrecognizes the significance of Cristina M. Rodr\u00edguez becoming the first Latina to lead Yale Law School and the inspiration her leadership provides to the legal profession;\n**(3)**\nacknowledges the importance of having leaders in academia who possess a deep mastery of the law and a commitment to public service; and\n**(4)**\nencourages all law professors, following the example of Dean Rodr\u00edguez, to\u2014\n**(A)**\ninvest in the success and mentorship of every student; and\n**(B)**\nhonestly and diligently teach the rule of law and the United States Constitution.",
      "versionDate": "2026-01-21",
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
        "name": "Education",
        "updateDate": "2026-01-26T14:53:55Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1012ih.xml"
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
      "title": "Recognizing and honoring Cristina M. Rodr\u00edguez for her historic appointment as dean of Yale Law School.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T09:18:20Z"
    },
    {
      "title": "Recognizing and honoring Cristina M. Rodr\u00edguez for her historic appointment as dean of Yale Law School.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T09:06:26Z"
    }
  ]
}
```
