# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2596?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2596
- Title: Saving the Forest Service's Workforce Act
- Congress: 119
- Bill type: S
- Bill number: 2596
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-12-05T21:42:57Z
- Update date including text: 2025-12-05T21:42:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2596",
    "number": "2596",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Saving the Forest Service's Workforce Act",
    "type": "S",
    "updateDate": "2025-12-05T21:42:57Z",
    "updateDateIncludingText": "2025-12-05T21:42:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:31:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2596is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2596\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Heinrich (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo institute a reduction in force moratorium at the Forest Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Saving the Forest Service's Workforce Act .\n#### 2. Reduction in force moratorium at the Forest Service\n##### (a) In general\nUntil on or after the date that full-year appropriations for the Forest Service for fiscal year 2026 have been enacted into law, the Secretary of Agriculture (acting through the Chief of the Forest Service) may not\u2014\n**(1)**\ninitiate or implement any reduction in force at the Forest Service; or\n**(2)**\nconduct an involuntary separation of any employee in the competitive service, any career employee in the excepted service, or any career appointee in the Senior Executive Service of the Forest Service except for cause on charges of misconduct, delinquency, or performance.\n##### (b) Application\nFor the purposes of carrying out subsection (a)\u2014\n**(1)**\nthe terms competitive service , excepted service , and career appointee have the meanings given those terms in sections 2102, 2103, and 3132(a), respectively, of title 5, United States Code; and\n**(2)**\nsuch subsection shall be in addition to any other authority with respect to adverse personnel actions, including chapter 75 of title 5, United States Code.",
      "versionDate": "2025-07-31",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-08-01",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "4853",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Saving the Forest Service's Workforce Act",
      "type": "HR"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-12T20:48:26Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2596is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Saving the Forest Service's Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Saving the Forest Service's Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to institute a reduction in force moratorium at the Forest Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:49Z"
    }
  ]
}
```
