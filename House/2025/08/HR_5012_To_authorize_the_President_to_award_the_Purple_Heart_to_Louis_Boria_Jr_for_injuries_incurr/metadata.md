# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5012
- Title: To authorize the President to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps.
- Congress: 119
- Bill type: HR
- Bill number: 5012
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2025-09-19T18:47:36Z
- Update date including text: 2025-09-19T18:47:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-19",
    "latestAction": {
      "actionDate": "2025-08-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5012",
    "number": "5012",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001200",
        "district": "9",
        "firstName": "Darren",
        "fullName": "Rep. Soto, Darren [D-FL-9]",
        "lastName": "Soto",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "To authorize the President to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps.",
    "type": "HR",
    "updateDate": "2025-09-19T18:47:36Z",
    "updateDateIncludingText": "2025-09-19T18:47:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-19",
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
          "date": "2025-08-19T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5012ih.xml",
      "text": "V\n119th CONGRESS\n1st Session\nH. R. 5012\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Mr. Soto introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the President to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps.\n#### 1. Authorization to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps\nNotwithstanding the criteria in section 1 of Executive Order 11016, the President is authorized to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps.",
      "versionDate": "2025-08-19",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T18:47:36Z"
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
      "date": "2025-08-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5012ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the President to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T08:13:08Z"
    },
    {
      "title": "To authorize the President to award the Purple Heart to Louis Boria, Jr., for injuries incurred during World War II and the Korean War while a member of the Marine Corps.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:05:25Z"
    }
  ]
}
```
