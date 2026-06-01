# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8526
- Title: To amend the Public Health Service Act to update quality standards for mammography facilities for the use of AI systems, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8526
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-19T15:52:41Z
- Update date including text: 2026-05-19T15:52:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8526",
    "number": "8526",
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
    "title": "To amend the Public Health Service Act to update quality standards for mammography facilities for the use of AI systems, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-19T15:52:41Z",
    "updateDateIncludingText": "2026-05-19T15:52:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:02:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8526ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8526\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Schweikert introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to update quality standards for mammography facilities for the use of AI systems, and for other purposes.\n#### 1. Updating quality standards for mammography facilities for use of AI systems\nSection 354(f)(1) of the Public Health Service Act ( 42 U.S.C. 263b(f)(1) ) is amended\u2014\n**(1)**\nin subparagraph (D)\u2014\n**(A)**\nin the matter preceding clause (i), by striking physician who and inserting physician, or a machine-learning or artificial intelligence system, that ; and\n**(B)**\nin clause (ii), by striking who and inserting that ; and\n**(2)**\nin subparagraph (G)(ii)(I), by striking signed by the interpreting physician .",
      "versionDate": "2026-04-27",
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
        "updateDate": "2026-05-19T15:52:40Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8526ih.xml"
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
      "title": "To amend the Public Health Service Act to update quality standards for mammography facilities for the use of AI systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T09:03:31Z"
    },
    {
      "title": "To amend the Public Health Service Act to update quality standards for mammography facilities for the use of AI systems, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T08:06:48Z"
    }
  ]
}
```
