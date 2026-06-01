# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6493
- Title: NOEM Act
- Congress: 119
- Bill type: HR
- Bill number: 6493
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2026-05-15T08:08:12Z
- Update date including text: 2026-05-15T08:08:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6493",
    "number": "6493",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001196",
        "district": "6",
        "firstName": "Seth",
        "fullName": "Rep. Moulton, Seth [D-MA-6]",
        "lastName": "Moulton",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "NOEM Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:12Z",
    "updateDateIncludingText": "2026-05-15T08:08:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6493ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6493\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Mr. Moulton introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo allow victims to sue Federal immigration enforcement officers for constitutional violations.\n#### 1. Short title\nThis Act may be cited as the National Oversight and Enforcement of Misconduct Act or the NOEM Act .\n#### 2. Civil action against person acting under federal immigration enforcement authority\n##### (a)\nSection 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) is amended\u2014\n**(1)**\nin the first sentence, by inserting of any Federal immigration enforcement authority or before of any State .",
      "versionDate": "2025-12-05",
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
        "name": "Immigration",
        "updateDate": "2026-01-20T14:46:22Z"
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
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6493ih.xml"
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
      "title": "To allow victims to sue Federal immigration enforcement officers for constitutional violations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:08:12Z"
    },
    {
      "title": "NOEM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NOEM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Oversight and Enforcement of Misconduct Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:53:21Z"
    }
  ]
}
```
