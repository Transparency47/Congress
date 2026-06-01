# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3765?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3765
- Title: FALCONS Act
- Congress: 119
- Bill type: HR
- Bill number: 3765
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-07-16T14:47:44Z
- Update date including text: 2025-07-16T14:47:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-05 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-05 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3765",
    "number": "3765",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "FALCONS Act",
    "type": "HR",
    "updateDate": "2025-07-16T14:47:44Z",
    "updateDateIncludingText": "2025-07-16T14:47:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T20:27:52Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-05T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3765ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3765\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Green of Tennessee introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit Federal service academies from providing training and education based on critical race theory or diversity, equity, and inclusion.\n#### 1. Short title\nThis Act may be cited as the Focusing Academies on Leadership and Cultivating Officers for National Security Act or the FALCONS Act .\n#### 2. Prohibition on training and education at Federal service academies regarding critical race theory, diversity, equity, and inclusion\nNo Federal funds may be obligated or expended to establish a curriculum, or to provide training or education based on critical race theory, diversity, equity, and inclusion at any of the following institutions:\n**(1)**\nThe United States Military Academy.\n**(2)**\nThe United States Naval Academy.\n**(3)**\nThe United States Air Force Academy.\n**(4)**\nThe United States Coast Guard Academy.\n**(5)**\nThe United States Merchant Marine Academy.",
      "versionDate": "2025-06-05",
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
        "updateDate": "2025-07-16T14:47:44Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3765ih.xml"
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
      "title": "FALCONS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FALCONS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Focusing Academies on Leadership and Cultivating Officers for National Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal service academies from providing training and education based on critical race theory or diversity, equity, and inclusion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T09:18:30Z"
    }
  ]
}
```
