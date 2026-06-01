# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/418
- Title: Ride-Along Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 418
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-05-22T17:29:12Z
- Update date including text: 2025-05-22T17:29:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-05-15 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Submitted in House
- Latest action: 2025-05-15: Submitted in House

## Actions

- 2025-05-15 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-05-15 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/418",
    "number": "418",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Ride-Along Resolution",
    "type": "HRES",
    "updateDate": "2025-05-22T17:29:12Z",
    "updateDateIncludingText": "2025-05-22T17:29:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-15T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres418ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 418\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Ms. Craig submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nRequiring Members of the House of Representatives to serve one shift in a passenger seat of a law enforcement vehicle observing the work day of a local law enforcement officer once during each term as a Member of the House, and for other purposes.\n#### 1. Short title\nThis resolution may be cited as the Ride-Along Resolution .\n#### 2. Requirement for Members of the House of Representatives to participate in one ride-along during each term of Congress\n##### (a) In general\nEach Member of the House of Representatives shall participate in one ride-along in the respective congressional district of the Member once during each term as a Member of the House.\n##### (b) Regulations\nThe Committee on House Administration shall promulgate regulations to carry out this resolution.\n##### (c) Violation\nIf the Committee on Ethics determines that a Member has not satisfied the requirement under subsection (a) by the deadline described in such subsection, the Committee shall\u2014\n**(1)**\npublish the name of the Member on a readily available, public list on the website of the Committee that identifies Members who have not satisfied such requirement; and\n**(2)**\ncause to be published in the Congressional Record information with respect to the failure of the Member to satisfy such requirement.\n##### (d) Definitions\nIn this section:\n**(1) Ride-Along**\nThe term ride-along means an arrangement for a Member of the House of Representatives to serve one shift in a passenger seat of a law enforcement vehicle observing the work day of a local law enforcement officer in the respective congressional district of such Member.\n**(2) Member of the House of Representatives**\nThe term Member of the House of Representatives includes a Delegate or Resident Commissioner to the Congress.\n##### (e) Effective date\nThis section shall apply with respect to the One Hundred Eighteenth Congress and each succeeding Congress.",
      "versionDate": "2025-05-15",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2025-05-22T17:29:12Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres418ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Ride-Along Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T08:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ride-Along Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T08:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Requiring Members of the House of Representatives to serve one shift in a passenger seat of a law enforcement vehicle observing the work day of a local law enforcement officer once during each term as a Member of the House, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T08:33:18Z"
    }
  ]
}
```
