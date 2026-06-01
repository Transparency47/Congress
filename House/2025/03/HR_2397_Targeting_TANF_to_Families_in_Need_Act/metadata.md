# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2397
- Title: Targeting TANF to Families in Need Act
- Congress: 119
- Bill type: HR
- Bill number: 2397
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-05-30T19:41:22Z
- Update date including text: 2026-05-30T19:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2397",
    "number": "2397",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Targeting TANF to Families in Need Act",
    "type": "HR",
    "updateDate": "2026-05-30T19:41:22Z",
    "updateDateIncludingText": "2026-05-30T19:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:07:30Z",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2397ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2397\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Smith of Nebraska (for himself and Mr. Moran ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend part A of title IV of the Social Security Act to target funds to families in need.\n#### 1. Short title\nThis Act may be cited as the Targeting TANF to Families in Need Act .\n#### 2. Targeting funds to families in need\n##### (a) In general\nSection 404 of the Social Security Act ( 42 U.S.C. 604 ) is amended by adding at the end the following:\n(l) Establishing a threshold for families in need A State to which a grant is made under section 403(a)(1) shall use the grant only to provide assistance or services to a family whose income is less than twice the poverty guidelines updated periodically in the Federal Register under section 673(2) of the Omnibus Budget Reconciliation Act of 1981 ( 42 U.S.C. 9902(2) ). .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on October 1, 2026.",
      "versionDate": "2025-03-27",
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
        "updateDate": "2025-04-07T13:36:07Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2397ih.xml"
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
      "title": "Targeting TANF to Families in Need Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Targeting TANF to Families in Need Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend part A of title IV of the Social Security Act to target funds to families in need.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:51Z"
    }
  ]
}
```
