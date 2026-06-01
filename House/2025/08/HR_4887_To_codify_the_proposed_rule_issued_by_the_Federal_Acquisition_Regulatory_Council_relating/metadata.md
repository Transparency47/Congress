# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4887?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4887
- Title: SIPS Act
- Congress: 119
- Bill type: HR
- Bill number: 4887
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-09-17T22:02:09Z
- Update date including text: 2025-09-17T22:02:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4887",
    "number": "4887",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "SIPS Act",
    "type": "HR",
    "updateDate": "2025-09-17T22:02:09Z",
    "updateDateIncludingText": "2025-09-17T22:02:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-08-05T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4887ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4887\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Issa introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo codify the proposed rule issued by the Federal Acquisition Regulatory Council relating to ending procurement and forced use of paper straws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Ineffective Paper Straws Act or the SIPS Act .\n#### 2. Ending procurement and forced use of paper straws\n##### (a) Requirement\nA covered agency that procures or provides for use a straw during the performance of a contract in a facility that is owned or leased by such covered agency shall ensure that any such straw has the strength and durability of a plastic straw.\n##### (b) Representation\nA person who submits a bid or offer to a covered agency shall represent, by submission of such bid or offer, that such person\u2014\n**(1)**\ndoes not have any policy promoting the use of a paper straw or penalizing the use of a plastic straw;\n**(2)**\nshall not provide any paper straw in the performance of any contract; and\n**(3)**\nshall ensure that any straw such person provides in the performance of any contract has the strength and durability of a plastic straw.\n##### (c) Covered agency defined\nIn this section, the term covered agency means\u2014\n**(1)**\nthe Office of Management and Budget;\n**(2)**\nthe Office of Federal Procurement Policy;\n**(3)**\nthe Department of Defense;\n**(4)**\nthe General Services Administration; and\n**(5)**\nthe National Aeronautics and Space Administration.",
      "versionDate": "2025-08-05",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-09-17T22:02:09Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4887ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SIPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T10:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SIPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T10:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Ineffective Paper Straws Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T10:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify the proposed rule issued by the Federal Acquisition Regulatory Council relating to ending procurement and forced use of paper straws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T10:18:20Z"
    }
  ]
}
```
