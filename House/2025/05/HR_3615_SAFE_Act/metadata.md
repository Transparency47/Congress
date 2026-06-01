# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3615
- Title: SAFE Act
- Congress: 119
- Bill type: HR
- Bill number: 3615
- Origin chamber: House
- Introduced date: 2025-05-26
- Update date: 2025-06-12T15:34:51Z
- Update date including text: 2025-06-12T15:34:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-26: Introduced in House
- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-26: Introduced in House

## Actions

- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Introduced in House
- 2025-05-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-26",
    "latestAction": {
      "actionDate": "2025-05-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3615",
    "number": "3615",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SAFE Act",
    "type": "HR",
    "updateDate": "2025-06-12T15:34:51Z",
    "updateDateIncludingText": "2025-06-12T15:34:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-26",
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
          "date": "2025-05-26T13:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3615ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3615\nIN THE HOUSE OF REPRESENTATIVES\nMay 26, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the obligation or expenditure of Federal funds to pay foreign governments and entities for the detention of certain individuals.\n#### 1. Short title\nThis Act may be cited as the Stop Aid for Foreign Expulsion Act or the SAFE Act .\n#### 2. Prohibition on obligation or expenditure of Federal funds for certain detentions of individuals\n##### (a) In general\nNo Federal funds may be obligated or expended to, directly or indirectly, pay a foreign government, agency of a foreign government, or foreign entity for the detention of an individual, if a court of the United States has determined that such detention violates the laws of the United States.\n##### (b) Foreign entity defined\nIn this section, the term foreign entity means an entity not organized under the laws of the United States or of any jurisdiction within the United States.",
      "versionDate": "2025-05-26",
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
        "name": "International Affairs",
        "updateDate": "2025-06-12T15:34:51Z"
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
      "date": "2025-05-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3615ih.xml"
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
      "title": "SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Aid for Foreign Expulsion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the obligation or expenditure of Federal funds to pay foreign governments and entities for the detention of certain individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:25Z"
    }
  ]
}
```
