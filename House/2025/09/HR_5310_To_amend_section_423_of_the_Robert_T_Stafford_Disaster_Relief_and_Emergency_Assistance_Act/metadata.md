# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5310?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5310
- Title: Fairness and Accountability of Appeals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5310
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-22T19:31:00Z
- Update date including text: 2025-09-22T19:31:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5310",
    "number": "5310",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Fairness and Accountability of Appeals Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-22T19:31:00Z",
    "updateDateIncludingText": "2025-09-22T19:31:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5310ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5310\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Ezell introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend section 423 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for reimbursement of attorney\u2019s fees under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness and Accountability of Appeals Act of 2025 .\n#### 2. Appeals of assistance decisions\nSection 423 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5189a ) is amended by adding at the end the following:\n(e) Attorney\u2019s fees In any case in which an applicant who requested an appeal under subsection (a) or arbitration under subsection (d) receives a favorable decision following such appeal or arbitration, the Administrator shall reimburse such applicant for any attorney\u2019s fees of the applicant relating to such appeal or arbitration. .",
      "versionDate": "2025-09-11",
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
        "name": "Emergency Management",
        "updateDate": "2025-09-22T19:31:00Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5310ih.xml"
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
      "title": "Fairness and Accountability of Appeals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness and Accountability of Appeals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 423 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for reimbursement of attorney's fees under certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:48:29Z"
    }
  ]
}
```
