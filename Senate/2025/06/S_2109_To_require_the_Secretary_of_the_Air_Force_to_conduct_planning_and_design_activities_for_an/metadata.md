# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2109
- Title: Dyess CDC Addition Design Authorization Act
- Congress: 119
- Bill type: S
- Bill number: 2109
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-07-17T15:37:21Z
- Update date including text: 2025-07-17T15:37:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2109",
    "number": "2109",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Dyess CDC Addition Design Authorization Act",
    "type": "S",
    "updateDate": "2025-07-17T15:37:21Z",
    "updateDateIncludingText": "2025-07-17T15:37:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T16:31:17Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2109is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2109\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Cruz introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of the Air Force to conduct planning and design activities for an addition to a child development center at Dyess Air Force Base, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dyess CDC Addition Design Authorization Act .\n#### 2. Planning and design activities for child development center addition at Dyess Air Force Base, Texas\n##### (a) Planning and design\n**(1) In general**\nThe Secretary of the Air Force shall conduct planning and design activities for a project for the construction of an addition at a child development center at Dyess Air Force Base, Texas.\n**(2) Amount of project**\nThe project for which planning and design activities are required under paragraph (1) shall be for an amount not to exceed $6,500,000, of which planning and design may not exceed nine percent.\n**(3) Design activities**\nDesign activities required under paragraph (1) shall\u2014\n**(A)**\nensure integration with existing facility systems, including fire alarms, fencing, utility infrastructure, and access control; and\n**(B)**\naccount for continued occupancy during construction, custom facility extension on both ends, and redesign of affected outdoor spaces such as playgrounds.\n##### (b) Use of existing amounts\nThe requirements under this section shall be carried out using amounts otherwise available for planning and design under the unspecified minor military construction authority of the Department of the Air Force.",
      "versionDate": "2025-06-18",
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
        "updateDate": "2025-07-17T15:37:21Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2109is.xml"
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
      "title": "Dyess CDC Addition Design Authorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dyess CDC Addition Design Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Air Force to conduct planning and design activities for an addition to a child development center at Dyess Air Force Base, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:01Z"
    }
  ]
}
```
