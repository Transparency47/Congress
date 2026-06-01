# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/152
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Labor relating to the Adverse Effect Wage Rate Methodology.
- Congress: 119
- Bill type: SJRES
- Bill number: 152
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-01T19:57:38Z
- Update date including text: 2026-04-01T19:57:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/152",
    "number": "152",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Labor relating to the Adverse Effect Wage Rate Methodology.",
    "type": "SJRES",
    "updateDate": "2026-04-01T19:57:38Z",
    "updateDateIncludingText": "2026-04-01T19:57:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T19:41:31Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres152is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 152\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Padilla introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Labor relating to the Adverse Effect Wage Rate Methodology.\nThat Congress disapproves the rule submitted by the Employment and Training Administration of the Department of Labor relating to the Adverse Effect Wage Rate Methodology for the Temporary Employment of H-2A Nonimmigrants in Non-Range Occupations in the United States (90 Fed. Reg. 47914 (October 2, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-03-26",
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
        "name": "Labor and Employment",
        "updateDate": "2026-04-01T19:57:38Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres152is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Labor relating to the Adverse Effect Wage Rate Methodology.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T06:18:29Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Labor relating to the Adverse Effect Wage Rate Methodology.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T10:56:30Z"
    }
  ]
}
```
