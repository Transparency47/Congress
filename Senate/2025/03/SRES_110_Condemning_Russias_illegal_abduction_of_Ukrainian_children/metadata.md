# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/110
- Title: A resolution condemning Russia's illegal abduction of Ukrainian children.
- Congress: 119
- Bill type: SRES
- Bill number: 110
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-05-14T23:56:01Z
- Update date including text: 2025-05-14T23:56:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1583-1584)
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1583-1584)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/110",
    "number": "110",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution condemning Russia's illegal abduction of Ukrainian children.",
    "type": "SRES",
    "updateDate": "2025-05-14T23:56:01Z",
    "updateDateIncludingText": "2025-05-14T23:56:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1583-1584)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T23:17:23Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres110is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 110\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Durbin submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCondemning Russia\u2019s illegal abduction of Ukrainian children.\nThat the Senate\u2014\n**(1)**\ncondemns the Russian Federation\u2019s abduction, forcible transfer, and facilitation of the illegal deportation of Ukrainian children; and\n**(2)**\nimplores the Russian Federation to work with the international community to ensure the return, without delay, of all forcibly transferred Ukrainian children to their families.",
      "versionDate": "2025-03-05",
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
        "updateDate": "2025-05-14T23:56:01Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres110is.xml"
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
      "title": "A resolution condemning Russia's illegal abduction of Ukrainian children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:30Z"
    },
    {
      "title": "A resolution condemning Russia's illegal abduction of Ukrainian children.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T11:56:16Z"
    }
  ]
}
```
