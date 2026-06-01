# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4530?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4530
- Title: STOP Shells Act
- Congress: 119
- Bill type: HR
- Bill number: 4530
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-09-27T08:05:43Z
- Update date including text: 2025-09-27T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4530",
    "number": "4530",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "STOP Shells Act",
    "type": "HR",
    "updateDate": "2025-09-27T08:05:43Z",
    "updateDateIncludingText": "2025-09-27T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:07:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "HI"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "HI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4530ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4530\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Self (for himself and Mr. Case ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo apply licensing requirements under the Export Control Reform Act of 2018 to subsidiaries of entities listed on the Entity List or Military End User List, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Suppressing Tactics of Prohibited Shells Act or the STOP Shells Act .\n#### 2. Application of licensing requirements under the Export Control Reform Act of 2018 to subsidiaries of entities listed on the Entity List or Military End User List\n##### (a) In general\nThe Secretary of Commerce is authorized to and shall apply the licensing requirement under the Export Control Reform Act of 2018 to affiliates owned 50 percent or more in aggregate, directly or indirectly, by an entity listed on the Entity List or the Military End User List.\n##### (b) Foreign Direct Product Rule Assessment\n**(1) In general**\nPrior to adding an entity to the Entity List or Military End User List, the Secretary of Commerce shall conduct an assessment to determine whether application of the Foreign Direct Product Rule to the licensing requirement for the entity would advance United States national security or foreign policy interests.\n**(2) Congressional notification**\nNot later than 2 days after adding an entity to the Entity List, the Secretary shall provide the appropriate congressional committees with the respective Foreign Direct Product Rule Assessment for the entity.\n##### (c) Waiver\n**(1) In general**\nSubject to subsection (d), the Secretary of Commerce is authorized to exempt, on a case-by-case basis, from the requirement set forth in subsection (a) any entity determined by the Secretary of Commerce, in consultation with the Secretaries of State, Defense, and Energy, whose exemption is in the national security interest of the United States.\n**(2) Congressional notification**\nNot later than 2 days after issuing a waiver under this subsection, the Secretary shall notify the appropriate congressional committees and include a detailed explanation of the national security or foreign policy interest that justified the waiver.\n##### (d) Definitions\nIn this section\u2014\n**(1)**\nthe term Entity List means the list maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations, or successor regulations;\n**(2)**\nthe term Military End User List means the list maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 7 to part 744 of title 15, Code of Federal Regulations, or successor regulations; and\n**(3)**\nthe term Foreign Direct Product Rule has the meaning as described in part 734.9 of title 15, Code of Federal Regulations, or successor regulations.",
      "versionDate": "2025-07-17",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T16:40:33Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4530ih.xml"
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
      "title": "STOP Shells Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP Shells Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Suppressing Tactics of Prohibited Shells Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To apply licensing requirements under the Export Control Reform Act of 2018 to subsidiaries of entities listed on the Entity List or Military End User List, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:18Z"
    }
  ]
}
```
