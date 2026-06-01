# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/70?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/70
- Title: A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.
- Congress: 119
- Bill type: SJRES
- Bill number: 70
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-08-01T18:29:45Z
- Update date including text: 2025-08-01T18:29:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/70",
    "number": "70",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.",
    "type": "SJRES",
    "updateDate": "2025-08-01T18:29:45Z",
    "updateDateIncludingText": "2025-08-01T18:29:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
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
      "actionDate": "2025-07-28",
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
          "date": "2025-07-29T00:13:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres70is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 70\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Mr. Sanders introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed export of certain defense articles to Israel.\nThat the following proposed export to Israel is prohibited:\n**(1)**\nThe export of the following firearms, parts, and components controlled under Category I of the United States Munitions List in the amount of $1,000,000 or more and described in Transmittal No. DDTC 23\u2013066, which was submitted to Congress pursuant to section 36(c) of the Arms Export Control Act ( 22 U.S.C. 2776(c) ) and communication of which was published in the Congressional Record on July 15, 2025 (Executive Communication 1305): 5,000 M5 Commando 5.56mm fully automatic rifles to M.R.D. Efram Investments Ltd in Israel for ultimate end use by the Israel National Police.",
      "versionDate": "2025-07-28",
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
        "updateDate": "2025-08-01T18:29:45Z"
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
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres70is.xml"
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
      "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:27Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T10:56:19Z"
    }
  ]
}
```
