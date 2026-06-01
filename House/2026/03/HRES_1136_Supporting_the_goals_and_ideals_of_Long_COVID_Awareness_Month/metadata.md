# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1136
- Title: Supporting the goals and ideals of "Long COVID Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1136
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-01T14:25:02Z
- Update date including text: 2026-04-01T14:25:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-25 - IntroReferral: Submitted in House
- 2026-03-25 - IntroReferral: Submitted in House
- Latest action: 2026-03-25: Submitted in House

## Actions

- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-25 - IntroReferral: Submitted in House
- 2026-03-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1136",
    "number": "1136",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Supporting the goals and ideals of \"Long COVID Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-04-01T14:25:02Z",
    "updateDateIncludingText": "2026-04-01T14:25:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T14:00:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1136ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1136\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mrs. Foushee submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals and ideals of Long COVID Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of Long COVID Awareness Month ;\n**(2)**\nrecognizes the importance of bringing awareness to the challenges of living with long COVID; and\n**(3)**\nexpresses support for more medical research on the causes of and treatments for long COVID.",
      "versionDate": "2026-03-25",
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
        "updateDate": "2026-04-01T14:25:01Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1136ih.xml"
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
      "title": "Supporting the goals and ideals of \"Long COVID Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T08:18:32Z"
    },
    {
      "title": "Supporting the goals and ideals of \"Long COVID Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T08:06:43Z"
    }
  ]
}
```
