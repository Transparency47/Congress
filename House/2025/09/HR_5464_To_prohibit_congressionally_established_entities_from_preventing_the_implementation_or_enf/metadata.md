# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5464
- Title: Net Metering Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 5464
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-11-18T16:19:17Z
- Update date including text: 2025-11-18T16:19:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5464",
    "number": "5464",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001103",
        "district": "",
        "firstName": "Pablo",
        "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
        "lastName": "Hern\u00e1ndez",
        "party": "D",
        "state": "PR"
      }
    ],
    "title": "Net Metering Protection Act",
    "type": "HR",
    "updateDate": "2025-11-18T16:19:17Z",
    "updateDateIncludingText": "2025-11-18T16:19:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5464ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5464\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Hern\u00e1ndez introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit congressionally established entities from preventing the implementation or enforcement of net metering service standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Net Metering Protection Act .\n#### 2. Prohibition of actions to prevent implementation or enforcement of net metering service standards\n##### (a) Prohibition\nNotwithstanding any other provision of law, if a State regulatory authority or nonregulated electric utility determines it is appropriate to implement the standard under section 111(d)(11) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d)(11) ), no commission, board, or other entity established by Congress may prohibit or otherwise obstruct such implementation or the enforcement of such standard by that State regulatory authority or nonregulated electric utility.\n##### (b) Definitions\nIn this section, the terms nonregulated electric utility and State regulatory authority have the meanings given those terms in section 3 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602 ).",
      "versionDate": "2025-09-18",
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
        "name": "Energy",
        "updateDate": "2025-11-18T16:19:17Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5464ih.xml"
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
      "title": "Net Metering Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Net Metering Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit congressionally established entities from preventing the implementation or enforcement of net metering service standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:17Z"
    }
  ]
}
```
