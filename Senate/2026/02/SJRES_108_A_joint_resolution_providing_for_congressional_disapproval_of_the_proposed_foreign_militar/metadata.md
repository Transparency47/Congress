# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/108
- Title: A joint resolution providing for congressional disapproval of the proposed foreign military sales to the Government of Ukraine of certain defense articles and services.
- Congress: 119
- Bill type: SJRES
- Bill number: 108
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-02-17T18:16:32Z
- Update date including text: 2026-02-17T18:16:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/108",
    "number": "108",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sales to the Government of Ukraine of certain defense articles and services.",
    "type": "SJRES",
    "updateDate": "2026-02-17T18:16:32Z",
    "updateDateIncludingText": "2026-02-17T18:16:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-02-12T21:28:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres108is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 108\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Paul introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed foreign military sales to the Government of Ukraine of certain defense articles and services.\nThat the following proposed foreign military sale to the Government of Ukraine is prohibited:\n**(1)**\nThe sale of the following defense articles and services, described in Transmittal No. 25\u2013105, submitted to Congress pursuant to section 36(b)(1) of the Arms Export Control Act ( 22 U.S.C. 2776(b)(1) ), and published in the Congressional Record on February 10, 2026: Class IX spare parts in support of U.S. Army-supplied vehicles and weapon systems, as well as other related elements of logistics and program support.",
      "versionDate": "2026-02-12",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2026-02-17T18:16:31Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres108is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sales to the Government of Ukraine of certain defense articles and services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-14T04:18:23Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sales to the Government of Ukraine of certain defense articles and services.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T11:56:25Z"
    }
  ]
}
```
