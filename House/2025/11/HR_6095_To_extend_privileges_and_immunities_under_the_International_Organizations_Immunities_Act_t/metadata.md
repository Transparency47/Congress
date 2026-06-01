# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6095?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6095
- Title: Gulf Diplomacy Act
- Congress: 119
- Bill type: HR
- Bill number: 6095
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-12-05T21:30:52Z
- Update date including text: 2025-12-05T21:30:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6095",
    "number": "6095",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Gulf Diplomacy Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:30:52Z",
    "updateDateIncludingText": "2025-12-05T21:30:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6095ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6095\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo extend privileges and immunities under the International Organizations Immunities Act to the Gulf Cooperation Council.\n#### 1. Short title\nThis Act may be cited as the Gulf Diplomacy Act .\n#### 2. Extension of privileges and immunities to Gulf Cooperation Council mission\nThe International Organizations Immunities Act ( 22 U.S.C. 288 et seq. ) is amended by adding at the end the following:\n18. Gulf Cooperation Council mission (a) The provisions of this Act may be extended to the Gulf Cooperation Council in the same manner, to the same extent, and subject to the same conditions, as they may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. (b) Under such terms and conditions as the President shall determine, consistent with the purposes of this Act, the President is authorized to extend, or enter into an agreement to extend, to the Gulf Cooperation Council, and to its members, the privileges and immunities enjoyed by diplomatic missions accredited to the United States, and by members of such missions, subject to corresponding conditions and obligations. .",
      "versionDate": "2025-11-18",
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
        "updateDate": "2025-12-05T21:30:52Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6095ih.xml"
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
      "title": "Gulf Diplomacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T02:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gulf Diplomacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T02:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To extend privileges and immunities under the International Organizations Immunities Act to the Gulf Cooperation Council.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T02:33:24Z"
    }
  ]
}
```
