# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7713?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7713
- Title: Combating Deceptive Practices in Assistance Programs Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7713
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-03-27T21:02:55Z
- Update date including text: 2026-03-27T21:02:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7713",
    "number": "7713",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Combating Deceptive Practices in Assistance Programs Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-27T21:02:55Z",
    "updateDateIncludingText": "2026-03-27T21:02:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:05:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7713ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7713\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Schweikert introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to ensure the appropriate availability of personal care services under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Combating Deceptive Practices in Assistance Programs Act of 2026 .\n#### 2. Ensuring the appropriate availability of personal care services under the Medicaid program\n##### (a) In general\nSection 1905(a)(24) of the Social Security Act ( 42 U.S.C. 1396d(a)(24) ) is amended by inserting who is unable to perform 3 or more activities of daily living (as defined in section 7702B(c)(2)(B) of the Internal Revenue Code of 1986) and after to an individual .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to medical assistance furnished on or after January 12, 2027.",
      "versionDate": "2026-02-25",
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
        "name": "Health",
        "updateDate": "2026-03-27T21:02:55Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7713ih.xml"
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
      "title": "Combating Deceptive Practices in Assistance Programs Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T09:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating Deceptive Practices in Assistance Programs Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to ensure the appropriate availability of personal care services under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T09:48:22Z"
    }
  ]
}
```
