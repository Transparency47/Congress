# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4815?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4815
- Title: District of Columbia National Guard Commanding General Residency Act
- Congress: 119
- Bill type: HR
- Bill number: 4815
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-09-12T20:16:53Z
- Update date including text: 2025-09-12T20:16:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4815",
    "number": "4815",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "District of Columbia National Guard Commanding General Residency Act",
    "type": "HR",
    "updateDate": "2025-09-12T20:16:53Z",
    "updateDateIncludingText": "2025-09-12T20:16:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4815ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4815\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the commanding general of the District of Columbia National Guard to reside in the District of Columbia.\n#### 1. Short title\nThis Act may be cited as the District of Columbia National Guard Commanding General Residency Act .\n#### 2. Requiring Commanding General of the District of Columbia National Guard reside in the District of Columbia\n##### (a) Requirement\nSection 7 of the Act entitled An Act to provide for the organization of the militia of the District of Columbia, and for other purposes , approved March 1, 1889 (sec. 49\u2013301, D.C. Official Code), is amended by adding at the end the following new subsection:\n(d) The Commanding General of the District of Columbia National Guard shall reside in the District of Columbia. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the day that is one year after the date of the enactment of this Act.",
      "versionDate": "2025-07-29",
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
        "updateDate": "2025-09-12T20:16:53Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4815ih.xml"
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
      "title": "District of Columbia National Guard Commanding General Residency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-03T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "District of Columbia National Guard Commanding General Residency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-03T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the commanding general of the District of Columbia National Guard to reside in the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-03T06:18:19Z"
    }
  ]
}
```
