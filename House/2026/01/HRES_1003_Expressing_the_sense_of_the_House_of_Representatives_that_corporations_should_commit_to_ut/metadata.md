# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1003
- Title: Expressing the sense of the House of Representatives that corporations should commit to utilizing the benefits of women in boards of directors and other senior management positions.
- Congress: 119
- Bill type: HRES
- Bill number: 1003
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-01-20T14:37:07Z
- Update date including text: 2026-01-20T14:37:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House
- Latest action: 2026-01-15: Submitted in House

## Actions

- 2026-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-15 - IntroReferral: Submitted in House
- 2026-01-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1003",
    "number": "1003",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that corporations should commit to utilizing the benefits of women in boards of directors and other senior management positions.",
    "type": "HRES",
    "updateDate": "2026-01-20T14:37:07Z",
    "updateDateIncludingText": "2026-01-20T14:37:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:03:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1003ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1003\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Beyer submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing the sense of the House of Representatives that corporations should commit to utilizing the benefits of women in boards of directors and other senior management positions.\nThat it is the sense of the House of Representatives that\u2014\n**(1)**\nthe citizens of the United States have a significant stake in promoting robust, sustainable economic growth;\n**(2)**\nsuch growth will be strengthened and accelerated by the ever-fuller inclusion of women in the United States workforce, at all levels of corporate management; and\n**(3)**\ncorporations in the United States should undertake a commitment to ever-fuller utilization of the talents, skills, and work ethic of women on boards of directors and in other senior management positions.",
      "versionDate": "2026-01-15",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-20T14:37:06Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1003ih.xml"
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
      "title": "Expressing the sense of the House of Representatives that corporations should commit to utilizing the benefits of women in boards of directors and other senior management positions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:43Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives that corporations should commit to utilizing the benefits of women in boards of directors and other senior management positions.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:06:24Z"
    }
  ]
}
```
