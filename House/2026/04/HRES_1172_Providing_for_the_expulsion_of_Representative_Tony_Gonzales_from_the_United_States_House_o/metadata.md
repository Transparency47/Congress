# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1172
- Title: Providing for the expulsion of Representative Tony Gonzales from the United States House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 1172
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-22T13:05:37Z
- Update date including text: 2026-04-22T13:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-04-14 - IntroReferral: Submitted in House
- Latest action: 2026-04-14: Submitted in House

## Actions

- 2026-04-14 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-04-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1172",
    "number": "1172",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Providing for the expulsion of Representative Tony Gonzales from the United States House of Representatives.",
    "type": "HRES",
    "updateDate": "2026-04-22T13:05:37Z",
    "updateDateIncludingText": "2026-04-22T13:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
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
      "actionCode": "1025",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
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
          "date": "2026-04-14T16:02:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1172ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1172\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Ms. Leger Fernandez submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nProviding for the expulsion of Representative Tony Gonzales from the United States House of Representatives.\nThat pursuant to article I, section 5, clause 2 of the Constitution of the United States, Representative Tony Gonzales, be, and he hereby is, expelled from the United States House of Representatives.",
      "versionDate": "2026-04-14",
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
        "updateDate": "2026-04-22T13:05:36Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1172ih.xml"
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
      "title": "Providing for the expulsion of Representative Tony Gonzales from the United States House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T08:18:32Z"
    },
    {
      "title": "Providing for the expulsion of Representative Tony Gonzales from the United States House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T08:06:05Z"
    }
  ]
}
```
