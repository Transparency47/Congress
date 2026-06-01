# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5190
- Title: To expand the contested logistics demonstration and prototyping program to include commercial additive manufacturing facilities in contested logistics environments, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5190
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-09-23T18:25:52Z
- Update date including text: 2025-09-23T18:25:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5190",
    "number": "5190",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To expand the contested logistics demonstration and prototyping program to include commercial additive manufacturing facilities in contested logistics environments, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-09-23T18:25:52Z",
    "updateDateIncludingText": "2025-09-23T18:25:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:03:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5190ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5190\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Khanna introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo expand the contested logistics demonstration and prototyping program to include commercial additive manufacturing facilities in contested logistics environments, and for other purposes.\n#### 1. Modification to demonstration and prototyping program to advance international product support capabilities in a contested logistics environment\nSection 842 of the National Defense Authorization Act for Fiscal Year 2024 ( Public Law 118\u201331 ; 10 U.S.C. 2341 note) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) commercial additive manufacturing facilities for rapid, distributed production of parts closer to the point of use; and ; and\n**(2)**\nin subsection (g), by striking on the date and all that follows and inserting December 31, 2030. .",
      "versionDate": "2025-09-08",
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
        "updateDate": "2025-09-23T18:25:52Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5190ih.xml"
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
      "title": "To expand the contested logistics demonstration and prototyping program to include commercial additive manufacturing facilities in contested logistics environments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:37Z"
    },
    {
      "title": "To expand the contested logistics demonstration and prototyping program to include commercial additive manufacturing facilities in contested logistics environments, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:05:18Z"
    }
  ]
}
```
