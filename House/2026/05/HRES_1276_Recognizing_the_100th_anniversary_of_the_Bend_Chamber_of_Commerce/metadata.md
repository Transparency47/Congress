# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1276
- Title: Recognizing the 100th anniversary of the Bend Chamber of Commerce.
- Congress: 119
- Bill type: HRES
- Bill number: 1276
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-21T20:28:07Z
- Update date including text: 2026-05-21T20:28:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-12 - IntroReferral: Submitted in House
- Latest action: 2026-05-12: Submitted in House

## Actions

- 2026-05-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1276",
    "number": "1276",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001326",
        "district": "5",
        "firstName": "Janelle",
        "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
        "lastName": "Bynum",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Recognizing the 100th anniversary of the Bend Chamber of Commerce.",
    "type": "HRES",
    "updateDate": "2026-05-21T20:28:07Z",
    "updateDateIncludingText": "2026-05-21T20:28:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionCode": "1025",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
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
          "date": "2026-05-12T16:02:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1276ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1276\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Ms. Bynum submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the 100th anniversary of the Bend Chamber of Commerce.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and celebrates the 100th anniversary of the Bend Chamber of Commerce and its century of contributions to the economic vitality and civic life of Bend, Oregon, and the Central Oregon region;\n**(2)**\ncommends the Bend Chamber of Commerce for its enduring commitment to supporting entrepreneurs, strengthening businesses, and fostering collaboration across the community;\n**(3)**\nhonors the generations of leaders, members, staff, and volunteers whose vision and service have shaped the Bend Chamber of Commerce over the past 100 years; and\n**(4)**\nencourages continued partnership among businesses, civic organizations, and public institutions to ensure a thriving and prosperous future for Bend and Central Oregon.",
      "versionDate": "2026-05-12",
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
        "name": "Commerce",
        "updateDate": "2026-05-21T20:28:07Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1276ih.xml"
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
      "title": "Recognizing the 100th anniversary of the Bend Chamber of Commerce.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:30Z"
    },
    {
      "title": "Recognizing the 100th anniversary of the Bend Chamber of Commerce.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:53Z"
    }
  ]
}
```
