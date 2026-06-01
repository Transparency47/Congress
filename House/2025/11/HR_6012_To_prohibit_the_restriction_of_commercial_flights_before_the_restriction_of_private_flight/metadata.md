# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6012
- Title: FARE Act
- Congress: 119
- Bill type: HR
- Bill number: 6012
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-01-07T09:05:38Z
- Update date including text: 2026-01-07T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-11 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-11 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6012",
    "number": "6012",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001196",
        "district": "6",
        "firstName": "Seth",
        "fullName": "Rep. Moulton, Seth [D-MA-6]",
        "lastName": "Moulton",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "FARE Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:38Z",
    "updateDateIncludingText": "2026-01-07T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-11",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-11T18:17:50Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6012ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6012\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Moulton introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo prohibit the restriction of commercial flights before the restriction of private flights during a lapse in appropriations.\n#### 1. Short title\nThis Act may be cited as the Fair Aviation in Restrictions and Emergencies Act or the FARE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Commercial flight**\nThe term commercial flight means a flight that is operated as a regularly scheduled flight by a passenger common carrier subject to Part 121 of Title 14, Code of Federal Regulations.\n**(2) Private aircraft flight**\nThe term private aircraft flight means a flight that is made using an aircraft equipped with 1 or more jet engines and that is not operated as a regularly scheduled flight by a passenger common carrier subject to Part 121 of Title 14, Code of Federal Regulations.\n#### 3. Prohibition on restriction of commercial flight operations during a lapse in appropriations\n##### (a) In general\nThe Federal Aviation Administration may not reduce or temporarily prohibit a commercial flight in the navigable airspace of the National Airspace System due to a lapse of appropriations, unless it has prohibited all private aircraft flights within the same geographical area for the same period of time.\n##### (b) Exceptions\nThe limitation in subsection (a) shall not apply to a private aircraft flight that is exclusively flown for\u2014\n**(1)**\na public safety purpose;\n**(2)**\ngovernment business;\n**(3)**\na military or diplomatic purpose;\n**(4)**\na medical reason;\n**(5)**\nan agricultural purpose;\n**(6)**\na meteorological or scientific purpose;\n**(7)**\nthe provision of humanitarian, nutritional, or emergency relief, including in response to a natural disaster; or\n**(8)**\nthe purpose of carrying cargo.\n##### (c) In general\nThe Federal Aviation Administration may enforce this section through an enforcement action seeking a civil penalty under section 46301(a) of title 49, United States Code, or through a civil action in United States District Court seeking to enjoin any air carrier from violating this section.",
      "versionDate": "2025-11-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-19T13:11:59Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6012ih.xml"
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
      "title": "FARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Aviation in Restrictions and Emergencies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the restriction of commercial flights before the restriction of private flights during a lapse in appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T08:18:22Z"
    }
  ]
}
```
