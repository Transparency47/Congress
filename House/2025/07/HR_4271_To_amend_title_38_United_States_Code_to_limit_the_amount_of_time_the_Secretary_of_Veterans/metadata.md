# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4271?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4271
- Title: VR&E Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 4271
- Origin chamber: House
- Introduced date: 2025-07-02
- Update date: 2025-07-29T20:32:57Z
- Update date including text: 2025-07-29T20:32:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-02: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2025-07-02: Introduced in House

## Actions

- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-02",
    "latestAction": {
      "actionDate": "2025-07-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4271",
    "number": "4271",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "VR&E Accountability Act",
    "type": "HR",
    "updateDate": "2025-07-29T20:32:57Z",
    "updateDateIncludingText": "2025-07-29T20:32:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-02",
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
          "date": "2025-07-02T13:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4271ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4271\nIN THE HOUSE OF REPRESENTATIVES\nJuly 2, 2025 Mr. Van Orden introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to limit the amount of time the Secretary of Veterans Affairs may extend the period of a vocational rehabilitation program for a veteran.\n#### 1. Short title\nThis Act may be cited as the VR&E Accountability Act .\n#### 2. Limitation on extension of a vocational rehabilitation program for a veteran\nSection 3105(c) of title 38, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking The Secretary and inserting (1) Subject to paragraph (2), the Secretary ;\n**(2)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) The Secretary may not, under this subsection, extend the period of a vocational rehabilitation program for a veteran so that such period exceeds ninety-six months until after the Secretary\u2014 (A) determines that extraordinary circumstances apply in the case of such veteran; and (B) submits to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives written notice of such extension and the extraordinary circumstances for such extension. .",
      "versionDate": "2025-07-02",
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
        "updateDate": "2025-07-29T20:32:57Z"
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
      "date": "2025-07-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4271ih.xml"
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
      "title": "To amend title 38, United States Code, to limit the amount of time the Secretary of Veterans Affairs may extend the period of a vocational rehabilitation program for a veteran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:31:29Z"
    },
    {
      "title": "VR&E Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VR&E Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T04:23:24Z"
    }
  ]
}
```
