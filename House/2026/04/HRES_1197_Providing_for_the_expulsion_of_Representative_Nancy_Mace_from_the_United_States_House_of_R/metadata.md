# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1197?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1197
- Title: Providing for the expulsion of Representative Nancy Mace from the United States House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 1197
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-22T15:05:56Z
- Update date including text: 2026-04-22T15:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-04-20 - IntroReferral: Submitted in House
- Latest action: 2026-04-20: Submitted in House

## Actions

- 2026-04-20 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-04-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1197",
    "number": "1197",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for the expulsion of Representative Nancy Mace from the United States House of Representatives.",
    "type": "HRES",
    "updateDate": "2026-04-22T15:05:56Z",
    "updateDateIncludingText": "2026-04-22T15:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:05:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1197ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1197\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Mills submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nProviding for the expulsion of Representative Nancy Mace from the United States House of Representatives.\nThat pursuant to Article I, Section 5, Clause 2 of the Constitution of the United States, Representative Nancy Mace, be, and she hereby is, expelled from the United States House of Representatives.",
      "versionDate": "2026-04-20",
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
        "updateDate": "2026-04-22T15:05:56Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1197ih.xml"
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
      "title": "Providing for the expulsion of Representative Nancy Mace from the United States House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T08:18:33Z"
    },
    {
      "title": "Providing for the expulsion of Representative Nancy Mace from the United States House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T08:05:47Z"
    }
  ]
}
```
