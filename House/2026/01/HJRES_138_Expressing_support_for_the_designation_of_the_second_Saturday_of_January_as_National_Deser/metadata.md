# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/138?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/138
- Title: Expressing support for the designation of the second Saturday of January as "National Desert Day".
- Congress: 119
- Bill type: HJRES
- Bill number: 138
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-01-12T16:56:39Z
- Update date including text: 2026-01-12T16:56:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/138",
    "number": "138",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of the second Saturday of January as \"National Desert Day\".",
    "type": "HJRES",
    "updateDate": "2026-01-12T16:56:39Z",
    "updateDateIncludingText": "2026-01-12T16:56:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-01-08T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres138ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 138\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Mr. Ruiz submitted the following joint resolution; which was referred to the Committee on Natural Resources\nJOINT RESOLUTION\nExpressing support for the designation of the second Saturday of January as National Desert Day .\nThat Congress\u2014\n**(1)**\nsupports the designation of National Desert Day and requests the President to issue a proclamation calling upon the people of the United States to observe such day with appropriate programs, ceremonies, and activities;\n**(2)**\nacknowledges that deserts are a crucial stop for migrating birds to spend the winter and are part of supporting global biodiversity;\n**(3)**\nreaffirms its advocacy for native landscapes by committing to reduce invasive plant species and continue to maintain a pollinator garden;\n**(4)**\nhonors the ongoing efforts by the United States to educate citizens on their role in conserving desert biodiversity; and\n**(5)**\nencourages the pursuit of policies that ensure the protection and preservation of the world\u2019s deserts.",
      "versionDate": "2026-01-08",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-12T16:56:38Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres138ih.xml"
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
      "title": "Expressing support for the designation of the second Saturday of January as \"National Desert Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:27Z"
    },
    {
      "title": "Expressing support for the designation of the second Saturday of January as \"National Desert Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T09:07:02Z"
    }
  ]
}
```
