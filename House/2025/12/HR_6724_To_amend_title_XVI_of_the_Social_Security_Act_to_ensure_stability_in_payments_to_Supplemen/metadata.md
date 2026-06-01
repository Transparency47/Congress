# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6724
- Title: Protecting Supplemental Security Income for Disaster Victims Act
- Congress: 119
- Bill type: HR
- Bill number: 6724
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-03-28T08:06:36Z
- Update date including text: 2026-03-28T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6724",
    "number": "6724",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Protecting Supplemental Security Income for Disaster Victims Act",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:36Z",
    "updateDateIncludingText": "2026-03-28T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6724ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6724\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Rulli (for himself and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVI of the Social Security Act to ensure stability in payments to Supplemental Security Income beneficiaries.\n#### 1. Short title\nThis Act may be cited as the Protecting Supplemental Security Income for Disaster Victims Act .\n#### 2. Disregard of payments received in settlement of certain claims\n##### (a) Income disregard\nSection 1612(b) of the Social Security Act ( 42 U.S.C. 1382a(b) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (25);\n**(2)**\nby striking the period at the end of paragraph (26) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(27) any amount received by such individual (or such spouse) in settlement of a claim of personal injury, physical sickness, or damage to, or depreciation of, property of such individual (or such spouse), including any amount so received, whether before, on, or after the date of the enactment of this paragraph, in settlement of the case styled In Re: East Palestine Train Derailment, CASE NO. 4:23\u2013CV\u201300242, in the United States District Court for the Northern District of Ohio. .\n##### (b) Resource disregard\nSection 1613(a) of such Act ( 42 U.S.C. 1382b(a) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (16);\n**(2)**\nby striking the period at the end of paragraph (17) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(18) for the month of receipt and every month thereafter, any amount received by such individual (or such spouse) in settlement of a claim of personal injury, physical sickness, or damage to, or depreciation of, property of such individual (or such spouse), including any amount so received, whether before, on, or after the date of the enactment of this paragraph, in settlement of the case styled In Re: East Palestine Train Derailment, CASE NO. 4:23\u2013CV\u201300242, in the United States District Court for the Northern District of Ohio. .\n##### (c) Effective date\nThe amendments made by this Act shall apply with respect to benefits payable for months beginning on or after the date of the enactment of this Act, except that, in the case of the settlement specified in sections 1612(b)(27) and 1613(a)(18) of the Social Security Act, the amendments shall also apply with respect to benefits paid for months beginning before such date of enactment.",
      "versionDate": "2025-12-15",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-09T15:18:05Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6724ih.xml"
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
      "title": "Protecting Supplemental Security Income for Disaster Victims Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T06:38:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Supplemental Security Income for Disaster Victims Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-07T06:38:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVI of the Social Security Act to ensure stability in payments to Supplemental Security Income beneficiaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-07T06:33:18Z"
    }
  ]
}
```
