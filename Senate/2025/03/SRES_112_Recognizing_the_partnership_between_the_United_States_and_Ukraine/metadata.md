# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/112
- Title: A resolution recognizing the partnership between the United States and Ukraine.
- Congress: 119
- Bill type: SRES
- Bill number: 112
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-05-08T14:02:50Z
- Update date including text: 2025-05-08T14:02:50Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/112",
    "number": "112",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A resolution recognizing the partnership between the United States and Ukraine.",
    "type": "SRES",
    "updateDate": "2025-05-08T14:02:50Z",
    "updateDateIncludingText": "2025-05-08T14:02:50Z"
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
          "date": "2025-03-05T23:46:13Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres112is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 112\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Blumenthal submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nRecognizing the partnership between the United States and Ukraine.\nThat the Senate\u2014\n**(1)**\nreaffirms the support of the United States for the sovereignty and territorial integrity of Ukraine in the face of the illegal invasion of its territory by the Russian Federation; and\n**(2)**\nreaffirms the bonds of friendship and shared values between the people of United States and allied fighting forces.",
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
        "updateDate": "2025-05-08T14:02:50Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres112is.xml"
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
      "title": "A resolution recognizing the partnership between the United States and Ukraine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:32Z"
    },
    {
      "title": "A resolution recognizing the partnership between the United States and Ukraine.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T11:56:15Z"
    }
  ]
}
```
