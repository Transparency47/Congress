# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2788?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2788
- Title: Safety Grant Consistency Act
- Congress: 119
- Bill type: S
- Bill number: 2788
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-09-29T13:26:35Z
- Update date including text: 2025-09-29T13:26:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2788",
    "number": "2788",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Safety Grant Consistency Act",
    "type": "S",
    "updateDate": "2025-09-29T13:26:35Z",
    "updateDateIncludingText": "2025-09-29T13:26:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T19:24:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2788is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2788\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the Secretary of Transportation from establishing new performance measures or regulatory or program requirements relating to highway safety grant programs, to require the Secretary of Transportation to ease certain requirements relating to those programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safety Grant Consistency Act .\n#### 2. Prohibitions and requirements relating to highway safety grant programs\n##### (a) Definitions\nIn this section:\n**(1) Highway safety grant programs**\nThe term highway safety grant programs means the programs under sections 402 and 405 of title 23, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Prohibitions; requirements\nNotwithstanding any other provision of law, the Secretary\u2014\n**(1)**\nmay not establish new performance measures or regulatory or program requirements relating to the highway safety grant programs not in effect before the date of enactment of this Act; and\n**(2)**\nshall ease or eliminate any requirement relating to the highway safety grant programs not explicitly authorized or required by an Act of Congress.",
      "versionDate": "2025-09-11",
      "versionType": "Introduced in Senate"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-29T13:26:35Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2788is.xml"
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
      "title": "Safety Grant Consistency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safety Grant Consistency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of Transportation from establishing new performance measures or regulatory or program requirements relating to highway safety grant programs, to require the Secretary of Transportation to ease certain requirements relating to those programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:18Z"
    }
  ]
}
```
