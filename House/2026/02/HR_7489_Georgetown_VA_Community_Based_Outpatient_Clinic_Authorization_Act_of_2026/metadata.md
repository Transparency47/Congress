# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7489
- Title: Georgetown VA Community-Based Outpatient Clinic Authorization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7489
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-03-07T09:06:32Z
- Update date including text: 2026-03-07T09:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7489",
    "number": "7489",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001051",
        "district": "31",
        "firstName": "John",
        "fullName": "Rep. Carter, John R. [R-TX-31]",
        "lastName": "Carter",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Georgetown VA Community-Based Outpatient Clinic Authorization Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-07T09:06:32Z",
    "updateDateIncludingText": "2026-03-07T09:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-02T15:15:46Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7489ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7489\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Carter of Texas introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo authorize the construction of a community-based outpatient clinic in Georgetown, Texas, as a major medical facility project of the Department of Veterans Affairs for fiscal year 2027, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Georgetown VA Community-Based Outpatient Clinic Authorization Act of 2026 .\n#### 2. Authorization of community-based outpatient clinic in Georgetown, Texas, as a major medical facility project of Department of Veterans Affairs\n##### (a) In general\nThe Secretary of Veterans Affairs may carry out a major medical facility project in fiscal year 2027 in Georgetown, Texas, that consists of the construction of a new community-based outpatient clinic in an amount not to exceed $96,448,066.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of Veterans Affairs for fiscal year 2027 or the year in which funds are appropriated for the Construction, Major Projects account, $96,448,066 for the project authorized in subsection (a).",
      "versionDate": "2026-02-11",
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
        "updateDate": "2026-02-23T17:21:42Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7489ih.xml"
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
      "title": "Georgetown VA Community-Based Outpatient Clinic Authorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Georgetown VA Community-Based Outpatient Clinic Authorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the construction of a community-based outpatient clinic in Georgetown, Texas, as a major medical facility project of the Department of Veterans Affairs for fiscal year 2027, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:42Z"
    }
  ]
}
```
