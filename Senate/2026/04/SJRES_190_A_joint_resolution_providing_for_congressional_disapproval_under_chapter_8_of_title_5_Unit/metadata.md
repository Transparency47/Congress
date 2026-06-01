# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/190
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Executive Office for Immigration Review relating to "Appellate Procedures for the Board of Immigration Appeals".
- Congress: 119
- Bill type: SJRES
- Bill number: 190
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-18T19:56:00Z
- Update date including text: 2026-05-18T19:56:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/190",
    "number": "190",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Executive Office for Immigration Review relating to \"Appellate Procedures for the Board of Immigration Appeals\".",
    "type": "SJRES",
    "updateDate": "2026-05-18T19:56:00Z",
    "updateDateIncludingText": "2026-05-18T19:56:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T15:03:47Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres190is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 190\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Kaine (for himself and Mr. Durbin ) introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Executive Office for Immigration Review relating to Appellate Procedures for the Board of Immigration Appeals .\nThat Congress disapproves the rule submitted by the Executive Office for Immigration Review relating to Appellate Procedures for the Board of Immigration Appeals (91 Fed. Reg. 5267 (February 6, 2026)), and such rule shall have no force or effect.",
      "versionDate": "2026-04-30",
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
        "name": "Immigration",
        "updateDate": "2026-05-18T19:56:00Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres190is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Executive Office for Immigration Review relating to \"Appellate Procedures for the Board of Immigration Appeals\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:39Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Executive Office for Immigration Review relating to \"Appellate Procedures for the Board of Immigration Appeals\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:27Z"
    }
  ]
}
```
