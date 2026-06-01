# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/348?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/348
- Title: A resolution declaring August 14, 2025, as "National Save Social Security Day".
- Congress: 119
- Bill type: SRES
- Bill number: 348
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2025-09-05T15:45:15Z
- Update date including text: 2025-09-05T15:45:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S4909-4910)
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S4909-4910)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/348",
    "number": "348",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A resolution declaring August 14, 2025, as \"National Save Social Security Day\".",
    "type": "SRES",
    "updateDate": "2025-09-05T15:45:15Z",
    "updateDateIncludingText": "2025-09-05T15:45:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S4909-4910)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T22:56:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres348is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 348\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Cassidy submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDeclaring August 14, 2025, as National Save Social Security Day .\nThat the Senate\u2014\n**(1)**\ndesignates August 14, 2025, as National Save Social Security Day in recognition of the 90th anniversary of the Social Security program and its enduring importance to the economic well-being of the United States;\n**(2)**\nencourages all people of the United States to reflect on the value of the Social Security program, to learn about its history and future challenges, and to participate in civic activities that promote the protection and strengthening of the program;\n**(3)**\nurges Federal, State, and local governments, educational institutions, advocacy groups, and the private sector to engage in outreach, educational initiatives, and community events on this day, fostering dialogue about the future of the Social Security program and the need for timely, bipartisan solutions; and\n**(4)**\ncalls upon Members of Congress to work in a bipartisan manner to develop and enact legislation that ensures the long-term solvency of the Social Security program and protects seniors, individuals with disabilities, and families in the United States for generations to come.",
      "versionDate": "2025-07-30",
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
        "name": "Social Welfare",
        "updateDate": "2025-09-05T15:45:15Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres348is.xml"
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
      "title": "A resolution declaring August 14, 2025, as \"National Save Social Security Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:23Z"
    },
    {
      "title": "A resolution declaring August 14, 2025, as \"National Save Social Security Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T10:56:21Z"
    }
  ]
}
```
