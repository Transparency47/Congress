# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7763?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7763
- Title: Protecting American History Act
- Congress: 119
- Bill type: HR
- Bill number: 7763
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-20T15:27:15Z
- Update date including text: 2026-03-20T15:27:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7763",
    "number": "7763",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001296",
        "district": "2",
        "firstName": "Brendan",
        "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
        "lastName": "Boyle",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Protecting American History Act",
    "type": "HR",
    "updateDate": "2026-03-20T15:27:15Z",
    "updateDateIncludingText": "2026-03-20T15:27:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7763ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7763\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Boyle of Pennsylvania (for himself, Mr. Evans of Pennsylvania , and Ms. Scanlon ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to restore interpretive and educational exhibits at Independence National Historical Park in Philadelphia, Pennsylvania.\n#### 1. Short title\nThis Act may be cited as the Protecting American History Act .\n#### 2. Restoration of interpretive exhibits at Independence National Historical Park\n##### (a) In general\nNot later than 15 days after the date of the enactment of this Act, the Secretary shall restore any covered exhibits at the Historical Park removed from public display after January 21, 2026, so that such covered exhibits appear as they did at the Historical Park on that date.\n##### (b) Prohibition on future removal\nThe Secretary may not add, remove, destroy, or otherwise alter covered exhibits at the Historical Park without the express authorization of Congress.\n##### (c) Definitions\nIn this Act:\n**(1) Covered exhibit**\nThe term covered exhibit means an interpretive or educational exhibit, sign, plaque, or other display.\n**(2) Historical Park**\nThe term Historical Park means the Independence National Historical Park in Philadelphia, Pennsylvania.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the National Park Service.",
      "versionDate": "2026-03-03",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-03-20T15:27:15Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7763ih.xml"
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
      "title": "Protecting American History Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T05:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting American History Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to restore interpretive and educational exhibits at Independence National Historical Park in Philadelphia, Pennsylvania.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T05:48:47Z"
    }
  ]
}
```
