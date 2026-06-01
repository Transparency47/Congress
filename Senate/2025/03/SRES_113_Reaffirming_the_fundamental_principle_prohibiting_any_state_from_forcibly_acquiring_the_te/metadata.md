# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/113
- Title: A resolution reaffirming the fundamental principle prohibiting any state from forcibly acquiring the territory of another state.
- Congress: 119
- Bill type: SRES
- Bill number: 113
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-05-08T13:59:24Z
- Update date including text: 2025-05-08T13:59:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1584)
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1584)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/113",
    "number": "113",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution reaffirming the fundamental principle prohibiting any state from forcibly acquiring the territory of another state.",
    "type": "SRES",
    "updateDate": "2025-05-08T13:59:24Z",
    "updateDateIncludingText": "2025-05-08T13:59:24Z"
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
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1584)",
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
          "date": "2025-03-06T00:21:44Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres113is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 113\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Welch submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nReaffirming the fundamental principle prohibiting any state from forcibly acquiring the territory of another state.\nThat the Senate reaffirms the fundamental principle that no state shall threaten or use force against the territorial integrity or political integrity of any other state.",
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
        "updateDate": "2025-05-08T13:59:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres113is.xml"
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
      "title": "A resolution reaffirming the fundamental principle prohibiting any state from forcibly acquiring the territory of another state.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:37Z"
    },
    {
      "title": "A resolution reaffirming the fundamental principle prohibiting any state from forcibly acquiring the territory of another state.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T11:56:14Z"
    }
  ]
}
```
