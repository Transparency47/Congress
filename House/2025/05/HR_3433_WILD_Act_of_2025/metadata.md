# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3433?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3433
- Title: WILD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3433
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-06-18T15:10:50Z
- Update date including text: 2025-06-18T15:10:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3433",
    "number": "3433",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "WILD Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-18T15:10:50Z",
    "updateDateIncludingText": "2025-06-18T15:10:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:06:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3433ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3433\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Donalds introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Wilderness Act to allow certain entities to use unmanned aircraft systems within wilderness areas, potential wilderness areas, and wilderness study areas.\n#### 1. Short title\nThis Act may be cited as the Wilderness Inclusion for Limited-use Drones Act of 2025 or the WILD Act of 2025 .\n#### 2. Use of unmanned aircraft systems within wilderness\nSection 4(d) of the Wilderness Act ( 16 U.S.C. 1133(d) ) is amended by adding at the end the following:\n(8) (A) A Federal, State, local, or Tribal agency may use and operate an unmanned aircraft system within a wilderness area designated by this Act, potential wilderness area, or wilderness study area identified pursuant to section 603 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1782 ) to\u2014 (i) carry out environmental monitoring and research activities, including with respect to harmful algal blooms and invasive species; (ii) carry out law enforcement and search and rescue activities, including such activities carried out by the U.S. Customs and Border Protection; and (iii) monitor the effects of a natural disaster. (B) In this paragraph: (i) The term natural disaster has the meaning given the term in section 602(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5195a(a) ). (ii) The term unmanned aircraft system has the meaning given the term in section 44801(12) of title 49, United States Code. .",
      "versionDate": "2025-05-15",
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
        "updateDate": "2025-06-18T15:10:50Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3433ih.xml"
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
      "title": "WILD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WILD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wilderness Inclusion for Limited-use Drones Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Wilderness Act to allow certain entities to use unmanned aircraft systems within wilderness areas, potential wilderness areas, and wilderness study areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:21Z"
    }
  ]
}
```
