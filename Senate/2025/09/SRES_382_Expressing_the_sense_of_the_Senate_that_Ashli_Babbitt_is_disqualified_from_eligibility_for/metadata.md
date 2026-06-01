# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/382
- Title: A resolution expressing the sense of the Senate that Ashli Babbitt is disqualified from eligibility for military funeral honors under section 985 of title 10, United States Code.
- Congress: 119
- Bill type: SRES
- Bill number: 382
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2025-09-24T17:00:29Z
- Update date including text: 2025-09-24T17:00:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S6539)
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S6539)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/382",
    "number": "382",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that Ashli Babbitt is disqualified from eligibility for military funeral honors under section 985 of title 10, United States Code.",
    "type": "SRES",
    "updateDate": "2025-09-24T17:00:29Z",
    "updateDateIncludingText": "2025-09-24T17:00:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Veterans' Affairs. (text: CR S6539)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T18:29:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres382is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 382\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Gallego submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nRESOLUTION\nExpressing the sense of the Senate that Ashli Babbitt is disqualified from eligibility for military funeral honors under section 985 of title 10, United States Code.\nThat it is the sense of the Senate that\u2014\n**(1)**\nAshli Babbitt\u2019s actions on January 6, 2021, constitute disqualifying conduct under section 985 of title 10, United States Code, the rendering of military funeral honors to her would bring discredit upon the Air Force, and she is not eligible for such honors; and\n**(2)**\nthe Senate reaffirms its gratitude to the law enforcement officers and other personnel who defended the Capitol on January 6, 2021, and rejects efforts to glorify or legitimize the actions of those who sought to overturn the Constitution of the United States.",
      "versionDate": "2025-09-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-12T16:22:30Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres382is.xml"
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
      "title": "A resolution expressing the sense of the Senate that Ashli Babbitt is disqualified from eligibility for military funeral honors under section 985 of title 10, United States Code.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T02:18:24Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that Ashli Babbitt is disqualified from eligibility for military funeral honors under section 985 of title 10, United States Code.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T10:56:23Z"
    }
  ]
}
```
