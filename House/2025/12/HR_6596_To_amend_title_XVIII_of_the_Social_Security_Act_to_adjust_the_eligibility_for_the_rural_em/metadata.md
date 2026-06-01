# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6596?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6596
- Title: To amend title XVIII of the Social Security Act to adjust the eligibility for the rural emergency hospital designation under the Medicare program.
- Congress: 119
- Bill type: HR
- Bill number: 6596
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-07T17:46:52Z
- Update date including text: 2026-01-07T17:46:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6596",
    "number": "6596",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001228",
        "district": "2",
        "firstName": "Derek",
        "fullName": "Rep. Schmidt, Derek [R-KS-2]",
        "lastName": "Schmidt",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "To amend title XVIII of the Social Security Act to adjust the eligibility for the rural emergency hospital designation under the Medicare program.",
    "type": "HR",
    "updateDate": "2026-01-07T17:46:52Z",
    "updateDateIncludingText": "2026-01-07T17:46:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:02:05Z",
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
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6596ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6596\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Schmidt (for himself and Mr. Estes ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to adjust the eligibility for the rural emergency hospital designation under the Medicare program.\n#### 1. Adjusting eligibility for rural emergency hospital designation under Medicare\nSection 1861(kkk)(3) of the Social Security Act ( 42 U.S.C. 1395x(kkk)(3) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking as of and inserting , at any point during the period beginning on January 1, 2015, and ending on ;\n**(2)**\nin subparagraph (A), by striking or at the end;\n**(3)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(C) was an off-campus outpatient department of a hospital (as defined in section 1833(t)(21)(B)) that\u2014 (i) was a dedicated emergency department (as defined in section 489.24(b) of title 42, Code of Federal Regulations (or any successor regulation)); and (ii) was located in a county (or equivalent unit of local government) in a rural area (as defined in section 1886(d)(2)(D)). .",
      "versionDate": "2025-12-10",
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
        "updateDate": "2026-01-07T17:46:52Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6596ih.xml"
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
      "title": "To amend title XVIII of the Social Security Act to adjust the eligibility for the rural emergency hospital designation under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:16Z"
    },
    {
      "title": "To amend title XVIII of the Social Security Act to adjust the eligibility for the rural emergency hospital designation under the Medicare program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T09:06:46Z"
    }
  ]
}
```
