# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1804?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1804
- Title: Presidential Airlift Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1804
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2025-06-20T12:32:09Z
- Update date including text: 2025-06-20T12:32:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Armed Services. (Sponsor introductory remarks on measure: CR S2973; text: CR S2973)
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Armed Services. (Sponsor introductory remarks on measure: CR S2973; text: CR S2973)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1804",
    "number": "1804",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Presidential Airlift Security Act of 2025",
    "type": "S",
    "updateDate": "2025-06-20T12:32:09Z",
    "updateDateIncludingText": "2025-06-20T12:32:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services. (Sponsor introductory remarks on measure: CR S2973; text: CR S2973)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T21:16:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "RI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1804is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1804\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mr. Schumer introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo prohibit the use of funds to procure or modify foreign aircraft for presidential airlift.\n#### 1. Short title\nThis Act may be cited as the Presidential Airlift Security Act of 2025 .\n#### 2. Prohibition on use of funds to procure or modify foreign aircraft for presidential airlift\nNone of the funds authorized to be appropriated or otherwise made available for fiscal year 2025 or fiscal year 2026 for the Department of Defense may be made available for the procurement, modification, restoration, or maintenance of an aircraft previously owned by a foreign government, an entity controlled by a foreign government, or a representative of a foreign government for the purposes of providing presidential airlift options.",
      "versionDate": "2025-05-19",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-20T12:32:09Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1804is.xml"
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
      "title": "Presidential Airlift Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-29T01:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Presidential Airlift Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of funds to procure or modify foreign aircraft for presidential airlift.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:33Z"
    }
  ]
}
```
