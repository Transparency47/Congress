# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1680
- Title: Virginia Wilderness Additions Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1680
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-10-29T06:08:15Z
- Update date including text: 2025-10-29T06:08:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 213.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 213.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1680",
    "number": "1680",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Virginia Wilderness Additions Act of 2025",
    "type": "S",
    "updateDate": "2025-10-29T06:08:15Z",
    "updateDateIncludingText": "2025-10-29T06:08:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 213.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-10-27T22:42:21Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T20:01:13Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-08T17:01:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1680is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1680\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Kaine (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo designate additions to the Rough Mountain Wilderness and the Rich Hole Wilderness of the George Washington National Forest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Virginia Wilderness Additions Act of 2025 .\n#### 2. Additions to rough mountain and rich hole wildernesses\n##### (a) Rough mountain addition\nSection 1 of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584; 114 Stat. 2057; 123 Stat. 1002) is amended by adding at the end the following:\n(21) Rough mountain addition Certain land in the George Washington National Forest comprising approximately 1,000 acres, as generally depicted as the Rough Mountain Addition on the map entitled GEORGE WASHINGTON NATIONAL FOREST\u2014South half\u2014Alternative I\u2014Selected Alternative Management Prescriptions\u2014Land and Resources Management Plan Final Environmental Impact Statement and dated March 4, 2014, which is incorporated in the Rough Mountain Wilderness Area designated by paragraph (1). .\n##### (b) Rich hole addition\n**(1) Potential wilderness designation**\nIn furtherance of the purposes of the Wilderness Act ( 16 U.S.C. 1131 et seq. ), certain land in the George Washington National Forest comprising approximately 4,600 acres, as generally depicted as the Rich Hole Addition on the map entitled GEORGE WASHINGTON NATIONAL FOREST\u2014South half\u2014Alternative I\u2014Selected Alternative Management Prescriptions\u2014Land and Resources Management Plan Final Environmental Impact Statement and dated March 4, 2014, is designated as a potential wilderness area for incorporation in the Rich Hole Wilderness Area designated by section 1(2) of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584).\n**(2) Wilderness designation**\nThe potential wilderness area designated by paragraph (1) shall be designated as wilderness and incorporated in the Rich Hole Wilderness Area designated by section 1(2) of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584) on the earlier of\u2014\n**(A)**\nthe date on which the Secretary of Agriculture (referred to in this section as the Secretary ) publishes in the Federal Register notice that the activities permitted under paragraph (4) have been completed; or\n**(B)**\nthe date that is 5 years after the date of enactment of this Act.\n**(3) Management**\nExcept as provided in paragraph (4), the Secretary shall manage the potential wilderness area designated by paragraph (1) in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ).\n**(4) Water quality improvement activities**\n**(A) In general**\nTo enhance natural ecosystems within the potential wilderness area designated by paragraph (1) by implementing certain activities to improve water quality and aquatic passage, as set forth in the Forest Service document entitled Decision Notice for the Lower Cowpasture Restoration and Management Project and dated December 2015, the Secretary may use motorized equipment and mechanized transport in the potential wilderness area until the date on which the potential wilderness area is incorporated into the Rich Hole Wilderness Area under paragraph (2).\n**(B) Requirement**\nIn carrying out subparagraph (A), the Secretary, to the maximum extent practicable, shall use the minimum tool or administrative practice necessary to carry out that subparagraph with the least amount of adverse impact on wilderness character and resources.",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1680rs.xml",
      "text": "II\nCalendar No. 213\n119th CONGRESS\n1st Session\nS. 1680\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Kaine (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nOctober 27, 2025 Reported by Mr. Boozman , without amendment\nA BILL\nTo designate additions to the Rough Mountain Wilderness and the Rich Hole Wilderness of the George Washington National Forest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Virginia Wilderness Additions Act of 2025 .\n#### 2. Additions to rough mountain and rich hole wildernesses\n##### (a) Rough mountain addition\nSection 1 of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584; 114 Stat. 2057; 123 Stat. 1002) is amended by adding at the end the following:\n(21) Rough mountain addition Certain land in the George Washington National Forest comprising approximately 1,000 acres, as generally depicted as the Rough Mountain Addition on the map entitled GEORGE WASHINGTON NATIONAL FOREST\u2014South half\u2014Alternative I\u2014Selected Alternative Management Prescriptions\u2014Land and Resources Management Plan Final Environmental Impact Statement and dated March 4, 2014, which is incorporated in the Rough Mountain Wilderness Area designated by paragraph (1). .\n##### (b) Rich hole addition\n**(1) Potential wilderness designation**\nIn furtherance of the purposes of the Wilderness Act ( 16 U.S.C. 1131 et seq. ), certain land in the George Washington National Forest comprising approximately 4,600 acres, as generally depicted as the Rich Hole Addition on the map entitled GEORGE WASHINGTON NATIONAL FOREST\u2014South half\u2014Alternative I\u2014Selected Alternative Management Prescriptions\u2014Land and Resources Management Plan Final Environmental Impact Statement and dated March 4, 2014, is designated as a potential wilderness area for incorporation in the Rich Hole Wilderness Area designated by section 1(2) of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584).\n**(2) Wilderness designation**\nThe potential wilderness area designated by paragraph (1) shall be designated as wilderness and incorporated in the Rich Hole Wilderness Area designated by section 1(2) of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584) on the earlier of\u2014\n**(A)**\nthe date on which the Secretary of Agriculture (referred to in this section as the Secretary ) publishes in the Federal Register notice that the activities permitted under paragraph (4) have been completed; or\n**(B)**\nthe date that is 5 years after the date of enactment of this Act.\n**(3) Management**\nExcept as provided in paragraph (4), the Secretary shall manage the potential wilderness area designated by paragraph (1) in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ).\n**(4) Water quality improvement activities**\n**(A) In general**\nTo enhance natural ecosystems within the potential wilderness area designated by paragraph (1) by implementing certain activities to improve water quality and aquatic passage, as set forth in the Forest Service document entitled Decision Notice for the Lower Cowpasture Restoration and Management Project and dated December 2015, the Secretary may use motorized equipment and mechanized transport in the potential wilderness area until the date on which the potential wilderness area is incorporated into the Rich Hole Wilderness Area under paragraph (2).\n**(B) Requirement**\nIn carrying out subparagraph (A), the Secretary, to the maximum extent practicable, shall use the minimum tool or administrative practice necessary to carry out that subparagraph with the least amount of adverse impact on wilderness character and resources.",
      "versionDate": "2025-10-27",
      "versionType": "Reported in Senate"
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
        "updateDate": "2025-06-11T13:55:56Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1680is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1680rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Virginia Wilderness Additions Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "title": "Virginia Wilderness Additions Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Virginia Wilderness Additions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate additions to the Rough Mountain Wilderness and the Rich Hole Wilderness of the George Washington National Forest, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:23Z"
    }
  ]
}
```
