# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8381?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8381
- Title: Safe Check-Ins for Immigrants Act
- Congress: 119
- Bill type: HR
- Bill number: 8381
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-28T15:33:33Z
- Update date including text: 2026-04-28T15:33:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8381",
    "number": "8381",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Safe Check-Ins for Immigrants Act",
    "type": "HR",
    "updateDate": "2026-04-28T15:33:33Z",
    "updateDateIncludingText": "2026-04-28T15:33:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:03:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8381ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8381\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Ms. Meng introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide an option for virtual periodic appearances for aliens pending a decision on whether the alien is to be removed from the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Check-Ins for Immigrants Act .\n#### 2. Virtual periodic appearances for aliens pending a decision on whether the alien is to be removed from the United States\nSection 236 of the Immigration and Nationality Act ( 8 U.S.C. 1226 ) is amended by adding at the end the following:\n(g) Virtual periodic appearances (1) In general The Secretary of Homeland Security shall permit an alien described in paragraph (2) to appear virtually by video teleconference to satisfy the requirement described in paragraph (2)(B). (2) Alien described An alien described in this paragraph is an alien who\u2014 (A) is released under subsection (a)(2); and (B) is required to appear before an immigration officer (or before a case manager pursuant to an alternatives to detention program) periodically pending a decision on whether the alien is to be removed from the United States as a condition of such release. .",
      "versionDate": "2026-04-20",
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
        "updateDate": "2026-04-28T15:33:33Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8381ih.xml"
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
      "title": "Safe Check-Ins for Immigrants Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Check-Ins for Immigrants Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to provide an option for virtual periodic appearances for aliens pending a decision on whether the alien is to be removed from the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:28Z"
    }
  ]
}
```
