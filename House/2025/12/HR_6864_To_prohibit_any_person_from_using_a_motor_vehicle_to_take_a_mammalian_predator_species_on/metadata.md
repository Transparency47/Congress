# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6864?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6864
- Title: SAW Act
- Congress: 119
- Bill type: HR
- Bill number: 6864
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-02-24T09:05:50Z
- Update date including text: 2026-02-24T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6864",
    "number": "6864",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001094",
        "district": "4",
        "firstName": "Val",
        "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
        "lastName": "Hoyle",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "SAW Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:50Z",
    "updateDateIncludingText": "2026-02-24T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:06:30Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6864ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6864\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Hoyle of Oregon (for herself, Mr. Lawler , Mrs. Dingell , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit any person from using a motor vehicle to take a mammalian predator species on Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Snowmobiles Aren\u2019t Weapons Act or the SAW Act .\n#### 2. Prohibiting use of a motor vehicle to intentionally take a mammalian predator species on Federal land\n##### (a) Prohibition\nExcept as provided in subsection (b), any person who intentionally uses a motor vehicle to harass, pursue, hunt, shoot, wound, kill, trap, capture, or collect a mammalian predator species on Federal land shall be fined not more than $10,000, imprisoned not more than 5 years, or both.\n##### (b) Exceptions\nA violation of subsection (a) has not occurred if a person engaged in conduct prohibited by subsection (a) to avoid injury or death to themselves or another person.\n##### (c) Investigation of violations\nThe Secretary of the Interior, or a person authorized by the Secretary\u2014\n**(1)**\nshall make such investigations as the Secretary deems necessary to determine whether any person has violated or is violating this Act; and\n**(2)**\nwhen conducting an investigation under this subsection\u2014\n**(A)**\nmay obtain assistance from the Federal Bureau of Investigation, the Department of the Treasury, and such other Federal agency as the Secretary determines appropriate; and\n**(B)**\nmay request and accept the assistance of State and local law enforcement and governmental agencies.\n##### (d) Definitions\nIn this Act\u2014\n**(1)**\nthe term Federal land means land owned by the United States, except land with respect to which title is held in trust by the United States for the benefit of an American Indian Tribe or an individual American Indian;\n**(2)**\nthe term motor vehicle means a self-propelled vehicle or a vehicle propelled or drawn by a self-propelled vehicle that is operated on a highway, on a railroad track, on the ground, in the water, or in the air; and\n**(3)**\nthe term mammalian predator has the meaning given such term by the Secretary of the Interior.",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-21T16:15:45Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6864ih.xml"
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
      "title": "SAW Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAW Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Snowmobiles Aren\u2019t Weapons Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit any person from using a motor vehicle to take a mammalian predator species on Federal land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:27Z"
    }
  ]
}
```
