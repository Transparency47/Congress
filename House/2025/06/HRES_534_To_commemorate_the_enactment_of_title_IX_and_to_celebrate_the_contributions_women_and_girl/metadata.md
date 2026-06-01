# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/534
- Title: To commemorate the enactment of title IX and to celebrate the contributions women and girls make in education and athletics.
- Congress: 119
- Bill type: HRES
- Bill number: 534
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-06-23 - IntroReferral: Submitted in House
- 2025-06-23 - IntroReferral: Submitted in House
- Latest action: 2025-06-23: Submitted in House

## Actions

- 2025-06-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-06-23 - IntroReferral: Submitted in House
- 2025-06-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/534",
    "number": "534",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "M001136",
        "district": "9",
        "firstName": "Lisa",
        "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
        "lastName": "McClain",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "To commemorate the enactment of title IX and to celebrate the contributions women and girls make in education and athletics.",
    "type": "HRES",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:00:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres534ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 534\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mrs. McClain submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nTo commemorate the enactment of title IX and to celebrate the contributions women and girls make in education and athletics.\nThat the House of Representatives\u2014\n**(1)**\ncommemorates the anniversary of the day title IX was signed into law;\n**(2)**\ncelebrates the women and girls who committed their lives toward advancing equal opportunity in school and athletics;\n**(3)**\ncelebrates the contributions of female athletes and the coaches and parents of female athletes; and\n**(4)**\nsupports protecting the rights of female athletes to compete on a fair and equal playing field.",
      "versionDate": "2025-06-23",
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
        "updateDate": "2025-07-09T15:15:58Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres534ih.xml"
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
      "title": "To commemorate the enactment of title IX and to celebrate the contributions women and girls make in education and athletics.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T08:49:26Z"
    },
    {
      "title": "To commemorate the enactment of title IX and to celebrate the contributions women and girls make in education and athletics.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T08:05:31Z"
    }
  ]
}
```
