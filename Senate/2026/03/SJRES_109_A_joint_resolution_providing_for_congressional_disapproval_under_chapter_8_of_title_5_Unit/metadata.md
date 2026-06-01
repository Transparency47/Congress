# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/109
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to "Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan".
- Congress: 119
- Bill type: SJRES
- Bill number: 109
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/109",
    "number": "109",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan\".",
    "type": "SJRES",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T16:19:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres109is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 109\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Lee (for himself and Mr. Curtis ) introduced the following joint resolution; which was read twice and referred to the Committee on Energy and Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan .\nThat Congress disapproves the rule submitted by the Bureau of Land Management relating to Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan (issued January 13, 2025, as a record of decision and approved resource management plan, and a letter of opinion from the Government Accountability Office dated January 15, 2026, printed in the Congressional Record on February 25, 2026, on pages S675\u2013677, concluding that such record of decision and approved resource management plan is a rule under the Congressional Review Act), and such rule shall have no force or effect.",
      "versionDate": "2026-03-04",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-04",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "151",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan\".",
      "type": "HJRES"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-03-09T23:25:39Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres109is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T03:48:23Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"Grand Staircase-Escalante National Monument Record of Decision and Approved Resource Management Plan\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T11:56:21Z"
    }
  ]
}
```
