# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5003
- Title: Equal Treatment of the District of Columbia Under the Rural Health Transformation Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5003
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2025-09-12T20:22:15Z
- Update date including text: 2025-09-12T20:22:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-19 - IntroReferral: Sponsor introductory remarks on measure. (CR E777)
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-19 - IntroReferral: Sponsor introductory remarks on measure. (CR E777)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5003",
    "number": "5003",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Equal Treatment of the District of Columbia Under the Rural Health Transformation Program Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-12T20:22:15Z",
    "updateDateIncludingText": "2025-09-12T20:22:15Z"
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
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E777)",
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
          "date": "2025-08-19T14:02:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5003ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5003\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXI of the Social Security Act to extend eligibility for allotments under the Rural Health Transformation Program to the District of Columbia.\n#### 1. Short title\nThis Act may be cited as the Equal Treatment of the District of Columbia Under the Rural Health Transformation Program Act of 2025 .\n#### 2. Extending Rural Health Transformation Program eligibility to the District of Columbia\n##### (a) In general\nSection 2105(h)(2)(D) of the Social Security Act ( 42 U.S.C. 1397ee(h)(2)(D) ) is amended by inserting and the District of Columbia after the 50 States each place it appears.\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply as if enacted on the date of the enactment of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ).",
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
        "name": "Health",
        "updateDate": "2025-09-12T20:22:15Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5003ih.xml"
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
      "title": "To amend title XXI of the Social Security Act to extend eligibility for allotments under the Rural Health Transformation Program to the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T10:08:09Z"
    },
    {
      "title": "Equal Treatment of the District of Columbia Under the Rural Health Transformation Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Equal Treatment of the District of Columbia Under the Rural Health Transformation Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T08:23:16Z"
    }
  ]
}
```
