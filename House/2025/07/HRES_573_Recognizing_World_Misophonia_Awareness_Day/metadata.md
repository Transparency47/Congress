# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/573?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/573
- Title: Recognizing World Misophonia Awareness Day.
- Congress: 119
- Bill type: HRES
- Bill number: 573
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-07-24T13:55:35Z
- Update date including text: 2025-07-24T13:55:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-07-10 - IntroReferral: Submitted in House
- 2025-07-10 - IntroReferral: Submitted in House
- Latest action: 2025-07-10: Submitted in House

## Actions

- 2025-07-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-07-10 - IntroReferral: Submitted in House
- 2025-07-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/573",
    "number": "573",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Recognizing World Misophonia Awareness Day.",
    "type": "HRES",
    "updateDate": "2025-07-24T13:55:35Z",
    "updateDateIncludingText": "2025-07-24T13:55:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:01:40Z",
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
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres573ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 573\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mrs. Kim (for herself and Mrs. Foushee ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing World Misophonia Awareness Day.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes World Misophonia Awareness Day to increase awareness and understanding of misophonia as a legitimate mental disorder that affects social and emotional well being;\n**(2)**\nsupports further research into the causes, prevalence, and treatment options for misophonia, including its neurological and genetic components;\n**(3)**\nsupports efforts to provide training to healthcare workers and mental health professionals on recognizing the effects and signs of misophonia to ensure timely, compassionate care; and\n**(4)**\nencourages the development of accommodations to those suffering with misophonia.",
      "versionDate": "2025-07-10",
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
        "updateDate": "2025-07-24T13:55:35Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres573ih.xml"
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
      "title": "Recognizing World Misophonia Awareness Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-11T08:18:24Z"
    },
    {
      "title": "Recognizing World Misophonia Awareness Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-11T08:05:22Z"
    }
  ]
}
```
