# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6200
- Title: ESSENTIAL Act
- Congress: 119
- Bill type: HR
- Bill number: 6200
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2025-12-05T15:26:05Z
- Update date including text: 2025-12-05T15:26:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6200",
    "number": "6200",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "ESSENTIAL Act",
    "type": "HR",
    "updateDate": "2025-12-05T15:26:05Z",
    "updateDateIncludingText": "2025-12-05T15:26:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6200ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6200\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. LaMalfa (for himself and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency and the Secretary of Transportation to repeal or rescind certain actions, initiatives, policies, and regulations related to engine idle start-stop technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eliminating Start-Stop Engine Nuisance Technologies that Impair Automobile Life Act or the ESSENTIAL Act .\n#### 2. Repeal of certain actions, initiatives, policies, and regulations related to engine idle start-stop technology\n##### (a) In general\nNotwithstanding any other provision of law (except subsection (b)), the Administrator of the Environmental Protection Agency and the Secretary of Transportation\u2014\n**(1)**\nshall, not later than 1 year after the date of enactment of this section, repeal or rescind any action, initiative, policy, or regulation of the Environmental Protection Agency or the Department of Transportation that is specifically designed to encourage, incentivize, promote, or require manufacturers of vehicles (including cars and trucks) to install or equip any such vehicle with engine idle start-stop technology; and\n**(2)**\nmay not issue, take, or enforce any action, initiative, policy, or regulation that is similar to an action, initiative, policy, or regulation that is repealed or rescinded under paragraph (1).\n##### (b) Exception\nNotwithstanding subsection (a), the Administrator of the Environmental Protection Agency and the Secretary of Transportation may not repeal or rescind any action, initiative, policy, or regulation if, at the determination of the Administrator or the Secretary, the repeal or rescission would result in increased risk of carbon monoxide poisoning.\n##### (c) Reports\n**(1) Initial report**\nNot later than 180 days after the date of enactment of this section, the Administrator of the Environmental Protection Agency and the Secretary of Transportation shall jointly submit to Congress a report that outlines how the Administrator and the Secretary are carrying out subsection (a)(1).\n**(2) Final report**\nNot later than 1 year after the date of enactment of this section, the Administrator of the Environmental Protection Agency and the Secretary of Transportation shall jointly submit to Congress a report that outlines how the Administrator and the Secretary carried out subsection (a)(1).\n##### (d) Engine idle start-Stop technology defined\nIn this section, the term engine idle start-stop technology means any technology which enables a vehicle to automatically turn off the engine when the vehicle comes to a rest and restarts the engine when the driver applies pressure to the accelerator or releases the brake.",
      "versionDate": "2025-11-20",
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-05T15:26:05Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6200ih.xml"
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
      "title": "ESSENTIAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T13:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ESSENTIAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T13:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eliminating Start-Stop Engine Nuisance Technologies that Impair Automobile Life Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T13:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency and the Secretary of Transportation to repeal or rescind certain actions, initiatives, policies, and regulations related to engine idle start-stop technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T13:03:44Z"
    }
  ]
}
```
