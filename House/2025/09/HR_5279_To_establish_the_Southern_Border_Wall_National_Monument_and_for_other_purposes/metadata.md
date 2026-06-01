# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5279?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5279
- Title: THE DON-ument Act
- Congress: 119
- Bill type: HR
- Bill number: 5279
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-09-18T16:34:42Z
- Update date including text: 2025-09-18T16:34:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5279",
    "number": "5279",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "THE DON-ument Act",
    "type": "HR",
    "updateDate": "2025-09-18T16:34:42Z",
    "updateDateIncludingText": "2025-09-18T16:34:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:07:20Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "AL"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5279ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5279\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Mills (for himself and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the Southern Border Wall National Monument, and for other purposes.\n#### 1. Short title\nThis Act may be cited as THE DON-ument Act .\n#### 2. Southern Border Wall National Monument\n##### (a) Establishment\nThere is hereby established, in the States of California, Arizona, New Mexico, and Texas, the Southern Border Wall National Monument to protect the southern border wall from alteration.\n##### (b) Area included\nThe National Monument shall consist of portions of the southern border wall and lands and interests therein comprising approximately 289,920 acres as generally depicted on the map entitled _________ , numbered ________, and dated __________.\n##### (c) Map\nThe map referred to in subsection (b) shall be on file and available for public inspection in the offices of the Bureau of Land Management, Department of the Interior.\n##### (d) Administration\n**(1) In general**\nThe Secretary, acting through the Director of the Bureau of Land Management, shall administer the National Monument.\n**(2) Administrative jurisdiction**\nThe Secretary shall establish administrative jurisdiction over portions of the southern border wall within the National Monument as necessary to carry out this Act by entering into memoranda of understanding with the following:\n**(A)**\nThe head of each Federal department or agency with administrative jurisdiction over land within the National Monument on which portions of the southern border wall are located.\n**(B)**\nThe governing body of each Indian Tribe with administrative jurisdiction over land within the National Monument on which portions of the southern border wall are located.\n##### (e) Management plan\n**(1) Deadline for completion**\nNot later than 3 years after the date on which funds are first made available to the Secretary for the preparation of a general management plan for the National Monument, the Secretary shall prepare a general management plan for the National Monument.\n**(2) Submission to Congress**\nOn completion of the general management plan under paragraph (1), the Secretary shall submit to the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate the general management plan under such paragraph.\n##### (f) Definitions\nIn this section:\n**(1) National Monument**\nThe term National Monument means the Southern Border Wall National Monument established in subsection (a).\n**(2) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(3) Southern border wall**\nThe term southern border wall means any portion of a physical wall constructed pursuant to Federal law or Executive order to serve as a barrier along the United States border with Mexico.",
      "versionDate": "2025-09-10",
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
        "updateDate": "2025-09-18T16:34:42Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5279ih.xml"
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
      "title": "THE DON-ument Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "THE DON-ument Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Southern Border Wall National Monument, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:18Z"
    }
  ]
}
```
