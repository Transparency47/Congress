# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/179?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/179
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to "Disclosure of Consumer Complaint Data".
- Congress: 119
- Bill type: SJRES
- Bill number: 179
- Origin chamber: Senate
- Introduced date: 2026-04-13
- Update date: 2026-04-20T19:09:34Z
- Update date including text: 2026-04-20T19:09:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-13: Introduced in Senate
- 2026-04-13 - IntroReferral: Introduced in Senate
- 2026-04-13 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-04-13: Introduced in Senate

## Actions

- 2026-04-13 - IntroReferral: Introduced in Senate
- 2026-04-13 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/179",
    "number": "179",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Disclosure of Consumer Complaint Data\".",
    "type": "SJRES",
    "updateDate": "2026-04-20T19:09:34Z",
    "updateDateIncludingText": "2026-04-20T19:09:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-13",
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
          "date": "2026-04-13T21:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres179is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 179\nIN THE SENATE OF THE UNITED STATES\nApril 13, 2026 Ms. Warren introduced the following joint resolution; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to Disclosure of Consumer Complaint Data .\nThat Congress disapproves the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to Disclosure of Consumer Complaint Data (78 Fed. Reg. 21218 (April 10, 2013)) (90 Fed. Reg. 20084 (May 12, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-04-13",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-20T19:09:34Z"
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
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres179is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Disclosure of Consumer Complaint Data\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T06:18:32Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Disclosure of Consumer Complaint Data\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T10:56:22Z"
    }
  ]
}
```
